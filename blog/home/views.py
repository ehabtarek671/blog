from django.shortcuts import render, get_object_or_404
from newblog.models import Post, Comment
from account.models import Account
from func.hash import md5hash
def index(req):
    return render(req, 'index.html')

def create(req):
    return render(req, 'create.html')

def post__(req, uuid):
    posts = get_object_or_404(Post, uuid=uuid)
    comments = Comment.objects.filter(post=posts)
    return render(req, 'post.html', {'post': posts, 'comments': comments})

def login(req):
    if req.method == 'GET':
        return render(req,'login.html')
    elif req.method == 'POST':
            email = req.POST.get('email')
            password = req.POST.get('pwd')
            account = Account.objects.filter(email = email, password=md5hash(password)).first()
            if account:
                req.session['email'] = email
                req.session['name'] = account.name
                req.session['profileimage'] = account.profile_image.url

def signup(req):
    if req.method == 'GET':
        return render(req,'signup.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        password = req.POST.get('pwd')
        account  = Account(name = name,email = email,password = password)
        account.save()