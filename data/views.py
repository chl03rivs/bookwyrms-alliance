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

    return render(
        request,
        "data/post_detail.html",
        {"post": post},
    )