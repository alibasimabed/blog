from django.shortcuts import render
from .models import Post
import os

# Create your views here.


def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        print(name)
        print(email)
        print(subject)
        print(message)

        
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts': posts})

def view_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog-single.html',{'post': post})
