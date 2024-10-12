# Imports
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from cloudinary.models import CloudinaryField

# User profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    gallery_picture = models.CharField(max_length=255, null=True, blank=True)  # To store selected gallery image

    def __str__(self):
        return self.user.username

    @property
    def user_picture(self):
        """
        Fetches the user's profile picture based on the three available choices:
           1. upload your own media (via Cloudinary)
           2. select a picture from the profile_gallery (static)
           3. no picture selected = placeholder image returned (static)
        """
        # 1. If user uploaded their own profile picture
        if self.profile_picture:
            return self.profile_picture.url
        # 2. If user selected a picture from the static gallery
        elif self.gallery_picture:
            return static(f'images/profile_gallery/{self.gallery_picture}')
        # 3. Otherwise, return the default placeholder image
        else:
            return static('images/profile_gallery/placeholder_profile_picture.webp')