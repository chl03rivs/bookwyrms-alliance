from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm

# CRUD views for posts and comments

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
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

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

def comment_edit(request, slug, comment_id):
    """
    View for comment updates:
        * author validation
        * form submission handling
        * pre-populating the form with current comment's data
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the post detail view 
        (To be added later: * flags the updated comment for review by the admins)
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
        {'comment_form': comment_form, 'post': post, 'comment': comment}
    )
