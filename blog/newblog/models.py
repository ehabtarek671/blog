from django.db import models
import uuid
import os

def user_profile_image_path(instance, filename):
    """Stores profile images in a folder named after the user's email."""
    return f'profile_images/{instance.email}/{filename}'

class Account(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=500, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    profile_image = models.ImageField(upload_to=user_profile_image_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    likes = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)
    active = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f'{self.title} by {self.author.name}'

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.author.name} on {self.post.title}'
