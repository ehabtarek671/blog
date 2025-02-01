from django.shortcuts import render, get_object_or_404
from newblog.models import Post, Comment

def index(req):
    return render(req, 'index.html')

def create(req):
    return render(req, 'create.html')

def post__(req, uuid):
    posts = get_object_or_404(Post, uuid=uuid)
    comments = Comment.objects.filter(post=posts)
    return render(req, 'post.html', {'post': posts, 'comments': comments})
