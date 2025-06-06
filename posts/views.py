from django.shortcuts import render
from .models import POST
# Create your views here.

def index(response):
    posts = POST.objects.all()
    return render(response, "index.html", {'posts': posts})

def post(response, pk):
    post = POST.objects.get(id = pk)
    return render(response, "posts.html", {'post': post})