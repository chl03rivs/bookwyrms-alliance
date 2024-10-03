from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from data.models import Post, Comment

# User profile
def profile_detail(request, user_id):
    '''
    Display an individual profile
    Uses template: users/account/profile_detail.html
    '''
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    # Fetch recent activity
    recent_posts = Post.objects.filter(user=user_profile.user).order_by('-created_on')[:5]
    recent_comments = Comment.objects.filter(user=user_profile.user).order_by('-created_on')[:5]
    
    context = {
        'profile': user_profile,
        'recent_posts': recent_posts,
        'recent_comments': recent_comments,
    }
    
    return render(request, 'users/profile_detail.html', context)