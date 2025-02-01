from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import uuid
from .models import Post
from  account.models import Account
import json
def create_post(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        content = req.POST.get('content')
        author = Account.objects.filter(email = req.session['email']).first()
        objects_number = Post.objects.all().count()
        post = Post(title=title,content=content,author=author,uuid = uuid.uuid5(namespace=uuid.NAMESPACE_URL,name = content+str(objects_number)+title+author.email))
        post.save()
        return redirect('/')
    elif req.method == 'PUT':       
        response = json.loads(req.body.decode('utf-8'))
        object_response = response.get('id')
        post_object = get_object_or_404(Post,uuid=object_response)
        post_object.active = False
        post_object.save()
        message_response = {'message':'Accepted'}
        return JsonResponse(message_response)

def addlike(req,uuid):
    if req.method == 'PUT':
        likenum = get_object_or_404(Post,uuid=uuid)
        likenum.likes+=1
        likenum.save()