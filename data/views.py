from django.shortcuts import render
from django.views import generic
from .models import Post

# Community posts: list view
class PostListView(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'templates/data/post_list.html'
    context_object_name = 'posts'