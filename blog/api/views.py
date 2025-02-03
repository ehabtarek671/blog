from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
import json
from newblog.models import Post,Account,Like,Dislike
from django.db.models import Q
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
        posts = Post.objects.all().filter(active = True)
        data = {
            "posts": [
                {
                    "title": post.title,
                    "content": post.content,
                    "url":post.uuid,
                    "author": post.author.name,
                    "views": post.views
                }
                for post in posts
            ]
        }

        return JsonResponse(data, safe=False) 

def NewLike(req):
    if req.method == 'POST':
        try:
            data = json.loads(req.body)
            uuid = data.get('uuid')
            account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
            post = Post.objects.filter(uuid = uuid).first()
            checklike = Like.objects.filter(Q(user_post_unique=account.email+post.title))
            if checklike.exists():
                checklike.delete()
            like = Like(user = account,post = post,user_post_unique=account.name+post.title)
            like.save()
            return JsonResponse({"message":"Accepted"})
        except Exception as e:
            return JsonResponse({'message':'Error','error':e})
    elif req.method == 'DELETE':
        try:
            data = json.loads(req.body)
            uuid = data.get('uuid')
            account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
            post = Post.objects.filter(uuid = uuid).first()
            like = Like.objects.filter(user = account,post = post).first()
            like.delete()
            return JsonResponse({"message":"Accepted"})
        except Exception as e:
            return JsonResponse({'message':'Error','error':e})

def NewDisLike(req):
    if req.method == 'POST':
        try:
            data = json.loads(req.body)
            uuid = data.get('uuid')
            account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
            post = Post.objects.filter(uuid = uuid).first()
            checklike = Dislike.objects.filter(Q(user_post_unique=account.email+post.title))
            if checklike.exists():
                checklike.delete()
            dislike = Dislike(user = account,post = post,user_post_unique=account.name+post.title)
            dislike.save()
            return JsonResponse({"message":"Accepted"})
        except Exception as e:
            return JsonResponse({'message':'Error','error':e})
    elif req.method == 'DELETE':
        try:
            data = json.loads(req.body)
            uuid = data.get('uuid')
            account = Account.objects.filter(email=req.COOKIES.get('email'),password=req.COOKIES.get('pwd')).first()
            post = Post.objects.filter(uuid = uuid).first()
            dislike = Dislike.objects.filter(user = account,post = post).first()
            dislike.delete()
            return JsonResponse({"message":"Accepted"})
        except Exception as e:
            return JsonResponse({'message':'Error','error':e})
        
def checklike(req,uuid):
    if req.method=='GET':
        post = Post.objects.filter(uuid=uuid).first()
        user = Account.objects.filter(email=req.COOKIES.get('email'),password = req.COOKIES.get('pwd')).first()
        like = Like.objects.filter(user = user,post=post).first()
        likebool = False
        dislike = Dislike.objects.filter(user = user,post=post).first()
        dislikebool = False
        if like:
            likebool=True
        if dislike:
            dislikebool=True
        data = {
            'like':likebool,
            'dislike':dislikebool
        }
        return JsonResponse(data=data,safe=False)
    else:
        return JsonResponse({'message':'error'})