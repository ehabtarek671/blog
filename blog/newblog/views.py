from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Post
import json
def create_post(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        author = req.POST.get('author')
        post = Post(title=title,content=content,author=author)
        post.save()
        return redirect('/')
    elif req.method == 'DELETE':
        
        response = json.loads(req.body.decode('utf-8'))
        object_response = response.get('id')
        post_object = Post
        post_object.objects.all().filter(pk = object_response).delete()
        message_response = {'message':'Accepted'}
        return JsonResponse(message_response)