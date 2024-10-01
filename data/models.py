from django.db import models
from users.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    post_title = models.CharField(max_length=255)
    # Commented out for now, until Google Books API is connected 
    # book = models.ForeignKey(Book)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Link to the post where the comment is made
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.post_title}'
