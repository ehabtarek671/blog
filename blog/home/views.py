from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from newblog.models import Post, Comment,Account,Like,Dislike
import datetime
import json
from func.hash import md5hash
def index(req):
    return  render(req, 'index.html')
def create(req):
    return render(req,'create.html')

def post__(req, uuid):
    posts = get_object_or_404(Post, uuid=uuid)
    comments = Comment.objects.filter(post=posts)
    return render(req, 'post.html', {'post': posts, 'comments': comments})

def login(req):
    if req.method == 'GET':
        return render(req,'login.html')
    elif req.method == 'POST':
            formdata = json.loads(req.body)
            email = formdata.get('email')
            password = md5hash(formdata.get('pwd'))
            account = Account.objects.filter(email = email, password=password).first()
            if account is None:
                return JsonResponse({'message':'Error'})
            else:
                data = JsonResponse({'message':'Accepted','email':email,'name':account.name,'profileImage':account.profile_image.url})
                if req.COOKIES.get('email')==None and req.COOKIES.get('pwd')==None:
                    data.set_cookie('email',email,expires=datetime.datetime.now()+datetime.timedelta(days=365.25))
                    data.set_cookie('pwd',password,expires=datetime.datetime.now()+datetime.timedelta(days=365.25))
                return data

def signup(req):
    if req.method == 'GET':
        return render(req,'signup.html')
    elif req.method == 'POST':
        try:
            name = req.POST.get('user_name')
            email = req.POST.get('user_email')
            password = md5hash(req.POST.get('user_password'))
            Image = req.FILES.get('user_image')
            account  = Account(name = name,email = email,password = password , profile_image = Image)
            account.save()
            return redirect('/login')
        except:
            return JsonResponse({'message':'Error'})