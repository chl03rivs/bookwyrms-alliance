# Imports
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# User profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder_profile_picture')
    gallery_picture = models.CharField(max_length=255, null=True, blank=True)  # To store selected gallery image

    def __str__(self):
        return self.user.username

    def get_profile_image(self):
        if self.profile_picture:
            return self.profile_picture.url
        elif self.gallery_picture:
            return f'static/images/profile_gallery/{self.gallery_picture}'
        else:
            return 'static/images/profile_gallery/placeholder_profile_picture.webp'