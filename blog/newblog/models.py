from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} by {self.author}'