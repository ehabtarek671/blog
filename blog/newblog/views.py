from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import uuid
from .models import Post, Account
import json

def create_post(req):
    if req.method == 'POST':
        email = req.COOKIES.get('email') 
        if email:
            author_account = Account.objects.filter(email=email).first()  
            if author_account:  
                title = req.POST.get('title')
                content = req.POST.get('content')
                
                if not title or not content:  # Ensure title and content are not empty
                    return JsonResponse({'error': 'Title and content are required'}, status=400)
                
                # Generate a unique UUID for each post
                unique_uuid = uuid.uuid4()

                # Create and save the Post object
                new_post = Post(title=title, content=content, author=author_account, uuid=unique_uuid)
                new_post.save()
                return redirect('/')
            else:
                return redirect('/create')  # Account not found
        else:
            return redirect('/login')  # Email not found in session
    elif req.method == 'PUT':
        data = json.loads(req.body)
        post_object = Post.objects.filter(pk = data['id']).first()
        post_object.active = False
        post_object.save()
        return JsonResponse({'message':'Accepted'})
def addlike(req,uuid):
    pass