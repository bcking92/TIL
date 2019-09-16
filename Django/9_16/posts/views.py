from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post, Comment


def index(request):
    post = Post.objects.all()
    context = {
        'post' : reversed(post),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        Post(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            updated_at = datetime.now(),
            ).save()

        return redirect('/post/')
    else:
        return render(request, 'create.html')


def detail(request, num):
    p = Post.objects.get(id=num)
    c = p.comment_set.all()
    context = {
        'p' : p,
        'c' : reversed(c),
    }
    return render(request, 'detail.html', context)


def update(request, num):
    p = Post.objects.get(id=num)

    if request.method == 'POST':
        p.title = request.POST.get('title'),
        p.content = request.POST.get('content'),
        p.updated_at = datetime.now(),
        p.save()
        return redirect('/post/')
    else:
        context = {
            'p' : p,
        }
        return render(request, 'update.html', context)

def delete(request, num):
    p = Post.objects.get(id=num)
    p.delete()
    return redirect('/post/')

def create_comment(request, num):
    p = Post.objects.get(id=num)
    Comment.objects.create(
        content=request.POST.get('content'),
        post=p,
    )
    return redirect(f'/post/detail/{num}/')