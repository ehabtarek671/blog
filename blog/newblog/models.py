from django.db import models
import uuid
from func.saveimage import user_profile_image_path
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
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    views = models.BigIntegerField(default=0)
    active = models.BooleanField(default=True,null=False)
    def __str__(self):
        return f'{self.title} by {self.author.name}'

class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user_post_unique = models.CharField(unique=True,max_length=500,default='000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} liked {self.post.title} made by {self.post.author.name}'

class Dislike(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='dislikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes')
    user_post_unique = models.CharField(unique=True,max_length=500,default='000')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} disliked {self.post.title} made by {self.post.author.name}'
class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.author.name} on {self.post.title}'
