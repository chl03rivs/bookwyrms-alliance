from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    profile_picture = CloudinaryField('image', default='profile_placeholder')

    def __str__(self):
        return self.user.username