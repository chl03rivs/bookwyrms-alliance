# Imports
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from allauth.account.forms import SignupForm

from .models import Post, Comment
from .forms import CommentForm, PostForm

# Home page
def home_view(request):
    # Retrieve the 7 most recent posts
    recent_posts = Post.objects.order_by('-created_at')[:7]
    
    context = {
        'recent_posts': recent_posts,
    }

    # Link sign up form
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            login(request, user)  # Automatically log in the user after registration
            return redirect('post_list')  # Redirect to the community after registration
    else:
        form = SignupForm()

    # Add the form to the context
    context['form'] = form

    return render(request, 'data/home.html', context)

# Help page
def help_view(request):
    return render(request, 'data/help.html')


# CRUD views for posts and comments
# Creating posts and comments
@login_required
def post_create(request):
    """
    View for creating new posts:
        * form submission handling
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the post detail view 
        
        (To be added later: * flags the newly created post for review by the admins)

    Uses template: `data/post_create.html`
    """
    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user  # Set the current user as the post's author
            post.save()
            messages.success(request, "Post created successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, "Error creating post. Please try again.")
    else:
        post_form = PostForm()

    return render(
        request,
        'data/post_create.html',
        {
            'post_form': post_form,
        }
    )

@login_required
def comment_create(request, slug):
    """
    View for creating a new comment on a specific post:
        * form submission handling
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the post detail view 
        
        (To be added later: * flags the newly created post for review by the admins)

    Uses template: `data/comment_create.html`
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user  # Set the current user as the comment's author
            comment.post = post  # Link the comment to the post
            comment.save()
            messages.success(request, "Comment added successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, "Error adding comment. Please try again.")
    else:
        comment_form = CommentForm()

    return render(
        request,
        'data/comment_create.html',
        {
            'comment_form': comment_form,
            'post': post,
        }
    )

# Reading/viewing content
class PostListView(generic.ListView):
    """
    List view of the community posts
    """
    queryset = Post.objects.all()
    template_name = 'templates/data/post_list.html'
    context_object_name = 'posts'

def post_detail(request, slug):
    """
    Display:
        * an individual Post
        * its comments
        * a comment count
    Uses template: data/post_detail.html
    """
    post = get_object_or_404(Post, slug=slug)

    # Use related_name to get comments
    comments = post.comments.all().order_by("-created_at")  # Comments ordered by newest first
    comment_count = post.comments.count()  # Total number of comments

    return render(
        request,
        "data/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )

# Updating content
@login_required
def comment_edit(request, slug, comment_id):
    """
    View for comment updates:
        * author validation
        * form submission handling
        * pre-populating the form with current comment's data
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the post detail view 
        
        (To be added later: * flags the updated comment for review by the admins)
    Uses template: `data/comment_edit.html`
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Only the author of the comment can edit it
    if comment.user != request.user:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('post_detail', slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # Make sure to link the comment to the post
            comment.save()

            messages.success(request, "Comment updated successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, "Error updating comment. Please try again.")
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        'data/comment_edit.html',
        {
            'comment_form': comment_form,
            'post': post,
            'comment': comment,
        }
    )

@login_required
def post_edit(request, slug):
    """
    View for post updates:
        * author validation
        * form submission handling
        * pre-populating the form with current post's data
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the post detail view 
        
        (To be added later: * flags the updated post for review by the admins)
    Uses template: `data/post_edit.html`
    """
    post = get_object_or_404(Post, slug=slug)

    # Only the author of the post can edit it
    if post.user != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('post_detail', slug=slug)

    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()

            messages.success(request, "Post updated successfully!")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, "Error updating post. Please try again.")
    else:
        post_form = PostForm(instance=post)

    return render(
        request,
        'data/post_edit.html',
        {
            'post_form': post_form, 
            'post': post,
        }
    )
# Deleting content
@login_required
def delete_post(request, post_id):
    """
    View for post deletion:
        * Only the post's author or an admin can delete it
        * uses Django's `messages` framework to provide success/error feedback to user
        * Renders confirmation page if accessed through a GET request
        * Redirects to the list of posts after deletion
    """
    post = get_object_or_404(Post, id=post_id)

    # Only allow deletion if the current user is the author or a superuser
    if post.user != request.user and not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('post_detail', slug=post.slug)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')

    return render(request, 'data/confirm_delete.html', {'post': post})

@login_required
def delete_comment(request, post_id, comment_id):
    """
    View for comment deletion:
        * Only the comment's author or an admin can delete the comment
        * uses Django's `messages` framework to provide success/error feedback to user
        * Renders confirmation page if accessed through a GET request
    """
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    # Only the author of the comment or an admin can delete it
    if comment.user != request.user and not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('post_detail', slug=post.slug)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('post_detail', slug=post.slug)

    return render(request, 'data/confirm_delete.html', {'comment': comment, 'post': post})
