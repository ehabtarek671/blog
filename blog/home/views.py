from django.shortcuts import render, get_object_or_404,redirect
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
            email = req.POST.get('user_email')
            password = req.POST.get('user_password')
            account = Account.objects.filter(email = email, password=password).first()
            if account is None:
                return redirect('/login')
            else:
                req.session['email'] = email
                req.session['name'] = account.name
                req.session['profileimage'] = account.profile_image.url
                return redirect('/')

def signup(req):
    if req.method == 'GET':
        return render(req,'signup.html')
    elif req.method == 'POST':
        name = req.POST.get('user_name')
        email = req.POST.get('user_email')
        password = req.POST.get('user_password')
        Image = req.FILES.get('user_image')
        account  = Account(name = name,email = email,password = password , profile_image = Image)
        account.save()
        req.session['email'] = email
        req.session['name'] = name
        return redirect('/')