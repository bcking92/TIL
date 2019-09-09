from django.shortcuts import render, redirect
from .models import Post


# Create your views here.

def home(request):
    temp = reversed(Post.objects.all())
    context = {
        'post': temp,
    }
    return render(request, 'home.html', context)

def created(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    img_url = request.GET.get('img_url')

    post = Post(title=title, content=content, img_url=img_url)
    post.save()
    return redirect('/home/')

def create(request):
    context = {

    }
    return render(request, 'create.html', context)

def delete(request, num):
    now = Post.objects.get(id=num)
    now.delete()
    return redirect('/home/')

def post(request, num):

    now = Post.objects.get(id=num)
    context = {
        'post' : now,
    }
    return render(request, 'post.html', context)

def update(request, num):
    now = Post.objects.get(id=num)
    context = {
        'post' : now,
    }
    return render(request, 'update.html', context)

def updated(request, num):
    post = Post.objects.get(id=num)
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.img_url = request.GET.get('img_url')

    
    post.save()
    return redirect('/home/')