from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import ProfileForm
from data.models import Post, Comment

# User profile
def profile_detail(request, user_id):
    '''
    View for individual user profile
    Uses template: `users/templates/account/profile_detail.html`
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
    
    return render(request, 'account/profile_detail.html', context)

@login_required
def edit(request, user_id):
    '''
    View for profile updates:
        * user validation
        * form submission handling
        * pre-populating the form with current profile data
        * uses Django's `messages` framework to provide success/error feedback to user
        * redirects back to the profile detail view 
        (To be added later: * flags the updated profile for review by the admins)

    Uses template: `users/templates/account/profile_edit.html`
    '''
    user_profile = get_object_or_404(UserProfile, user_id=user_id)

    # Only the owner of the profile can edit it
    if user_profile.user != request.user:
        messages.error(request, "You are not authorized to edit this profile.")
        
        return redirect('profile_detail', user_id=user_id)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")

            return HttpResponseRedirect(reverse('profile_detail', args=[user_id]))  # Redirect to profile detail view with the correct user_id
        else:
            messages.error(request, "Error updating profile. Please try again.")
    else:
        profile_form = ProfileForm(instance=user_profile)

    return render(
        request,
        'account/profile_edit.html',
        {
            'profile_form': profile_form,
            'user_profile': user_profile,
        }
    )