from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    # Commented out for now: requires Pillow
    # profile_picture = models.ImageField(blank=True, upload_to='media/profile_pics')

    def __str__(self):
        return self.user.username