from django.db import models
import uuid
from account.models import Account
from func.saveimage import user_profile_image_path
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts',blank=True,null=True)
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
