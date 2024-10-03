"""
URL configuration for the `data` app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]