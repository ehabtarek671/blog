from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from newblog.models import Post,Account,Like,DisLike

def send_user(req):
    if 'email' and 'pwd'  in req.COOKIES:
        account = Account.objects.filter(email = req.COOKIES.get('email') , password = req.COOKIES.get('pwd')).first()
        data = {
            'name':account.name,
            'email':account.email,
            'profileimage':account.profile_image.url
        }
        return JsonResponse(data,safe=False)
    else:
        return JsonResponse({'message':'error'},safe=False)
def send_posts(req):
    if req.method == 'GET':
        posts = Post.objects.all().filter(active = True)  # Get all posts

        data = {
            "posts": [
                {
                    "title": post.title,
                    "content": post.content,
                    "url":post.uuid,
                    "author": post.author.name,
                    "likes": post.likes,
                    "views": post.views
                }
                for post in posts
            ]
        }

        return JsonResponse(data, safe=False)  # Allow returning lists

def NewLike(req,uuid):
    if req.method == 'PUT':
        account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
        post = Post.objects.filter(uuid = uuid).first()
        like = Like(user = account,post = post)
        like.save()
    elif req.method == 'DELETE':
        account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
        post = Post.objects.filter(uuid = uuid).first()
        like = Like.objects.filter(user = account,post = post).first()
        like.delete()

def NewDisLike(req,uuid):
    if req.method == 'PUT':
        account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
        post = Post.objects.filter(uuid = uuid).first()
        dislike = DisLike(user = account,post = post)
        dislike.save()
    elif req.method == 'DELETE':
        account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
        post = Post.objects.filter(uuid = uuid).first()
        dislike = DisLike.objects.filter(user = account,post = post).first()
        dislike.delete()