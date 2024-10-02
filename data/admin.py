from django.contrib import admin
from .models import Post, Comment, Categories

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categories)