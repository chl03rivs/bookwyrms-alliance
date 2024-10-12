"""
URL configuration for the `data` app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/new_comment/', views.comment_create, name='new_comment')
]