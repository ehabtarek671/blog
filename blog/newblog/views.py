from django.shortcuts import render,redirect
from .models import Post
def create_post(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        author = req.POST.get('author')
        post = Post(title=title,content=content,author=author)
        post.save()
    elif req.method == 'DELETE':
        Post_obj = Post(pk = req.DELETE.get('id'))
        return redirect('/')