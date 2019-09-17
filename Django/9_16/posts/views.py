from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post, Comment


def index(request):
    post = Post.objects.all()
    context = {
        'post' : post,
        
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        Post(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            updated_at = datetime.now(),
            image = request.FILES.get('image')
            ).save()

        return redirect('/post/')
    else:
        return render(request, 'create.html')


def detail(request, num):
    p = Post.objects.get(id=num)
    c = p.comment_set.all()
    context = {
        'p' : p,
        'c' : c,
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
    a = request.POST.get('content')[:300]
    Comment.objects.create(
        content=a,
        post=p,
    )
    return redirect(f'/post/detail/{num}/')

def delete_comment(request, num):
    c = Comment.objects.get(id=num)
    a = c.post.id
    c.delete()
    return redirect(f'/post/detail/{a}/')

def update_comment(request, num):
    if request.method == "POST":
        c = Comment.objects.get(id=num)
        c.content = request.POST.get('content')
        c.save()
        return redirect(f'/post/detail/{c.post.id}/')
    else:
        c = Comment.objects.all()
        target = Comment.objects.get(id=num)
        p = target.post
        context = {
            'c' : c,
            'p' : p,
            'target' : target,
        }
        return render(request, 'update_comment.html', context)
