# Imports
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from users.models import UserProfile

# Posts        
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('opinion', 'Opinion'),
        ('rec', 'Recommendation'),
        ('disc', 'Discussion'),
        ('rant', 'Rant'),
        ('gtech', 'Gadgets & Tech'),
        ('hobbies', 'Hobbies'),
        ('writers', 'Writers'),
        ('misc', 'Miscellaneous'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    featured_image = CloudinaryField('image', default='placeholder')
    post_title = models.CharField(max_length=255)

    # Commented out for now, until Google Books API is connected 
    # linked_book = models.ForeignKey(Book)
    
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='discussion')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

    # Auto-generate slug from the post's title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)

# Comments
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user's profile
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Link to the post where the comment is made
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.post_title}'
