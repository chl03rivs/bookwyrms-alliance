'''
URL configuration for the `users` app
'''
# Imports
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Includes all the Allauth views
    path('profile/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
]