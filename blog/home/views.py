from django.shortcuts import render, get_object_or_404
from newblog.models import Post, Comment

def index(req):
    return render(req, 'index.html')

def create(req):
    return render(req, 'create.html')

def post(req, uuid):
    object_post = get_object_or_404(Post, uuid=uuid)
    comments = Comment.objects.filter(posts=object_post)
    return render(req, 'post.html', {'post': object_post, 'comments': comments})
