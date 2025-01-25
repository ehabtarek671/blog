from django.shortcuts import render

def index(req):
    return render(req,'index.html')

def create(req):
    return render(req,'create.html')
