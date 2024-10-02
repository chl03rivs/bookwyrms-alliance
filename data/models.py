from django.db import models
from users.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    post_title = models.CharField(max_length=255)
    # Commented out for now, until Google Books API is connected 
    # book = models.ForeignKey(Book)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)  # Link to Categories model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

    # Auto-generate slug from the post's title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Link to the post where the comment is made
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.post_title}'
