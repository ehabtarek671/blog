from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from newblog.models import Post,Account

def send_user(req):
    if 'email'  in req.session:
        data = {
            'name':req.session['name'],
            'email':req.session['email'],
            'profileimage':req.session['profileimage']
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
