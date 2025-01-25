from django.shortcuts import render,redirect
from django.http import HttpResponse
from newblog.models import Post
from django.core import serializers
def send_posts(req):
    if req.method == 'GET':
        data = Post
        query_set = data.objects.all()
        data = serializers.serialize('json',query_set)
        return HttpResponse(data)