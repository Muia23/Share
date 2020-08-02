from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    posts = Post.get_posts()
    return render(request,'home.html', {"posts": posts})
