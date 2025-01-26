from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=100)
    uuid = models.UUIDField(null=False,primary_key=True)
    def __str__(self):
        return f'{self.title} by {self.author}'
    
class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE)
    related_name="comments"

    def __str__(self):
        return f'{self.author} to {self.posts.title} by {self.posts.author}'