from django import forms
from .models import UserProfile

# User profile update
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'website', 'profile_picture')