
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

def BASE(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'home.html')

def home(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, '/home.html', context)