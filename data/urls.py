"""
URL configuration for the `data` app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('new_post/', views.post_create, name='new_post'),
    path('post/<int:post_id>/post_edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/new_comment/', views.comment_create, name='new_comment')
]