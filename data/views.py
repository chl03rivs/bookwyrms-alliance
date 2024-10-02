from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostListView(generic.ListView):
    """
    List view of the community posts
    """
    queryset = Post.objects.all()
    template_name = 'templates/data/post_list.html'
    context_object_name = 'posts'

def post_detail(request, slug):
    """
    Display an individual :model:`data.Post`.
    **Context**
    ``post``
        An instance of :model:`data.Post`.
    **Template:**
    :template:`data/post_detail.html`
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