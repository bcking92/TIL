from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : reversed(posts),
    }
    return render(request, 'posts/home.html', context)

def new(request):
    context = {
        
    }
    return render(request, 'posts/new.html', context)

def create(request):
    # request.GET
    # {'title' : 날아온데이터, 'content' : 날아온 데이터, ...}


    # new에서 날아온 data를 DB에 저장한다.
    post = Post()
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.img_url = request.GET.get('img_url')
    post.save()

    # save 따로안해도 되니까 무조건 create 쓰는게 이득아님?
    # 응, 아니야 validation 이 안된채로 걍 들어가버림 데이터 크기나, 형태가 스키마랑 다르게 들어가버림

    # Post.objects.create(
    #         title = request.GET.get('title'),
    #         content = request.GET.get('content'),
    #         img_url = request.GET.get('img_url'),
    # )

    # Post.objects.create(**request.GET)
    # 이렇게 해도 된다. 하지만 일단 한번에 알아보기가 어렵고, 어떤 데이터가 날라오는지 찾아야 하고, 걸러야될 데이터를 거르기 힘듬.
    return redirect('home')

def detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {
        'post' :post,
    }
    return render(request, 'posts/detail.html', context)

def delete(request,pk):
    # pk라는 id를 가진 글을 삭제
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')

def edit(request,pk):
    # pk라는 id를 가진 글을 편집하게 함
    # 1. pk라는 id를 가진 글을 찾음
    post = Post.objects.get(id=pk)

    context = {
        'post' : post,
    }
    return render(request, 'posts/edit.html', context)

def update(request, pk):
    # 1. pk라는 아이디를 가진 글을 찾아서,
    # 2. /edit/으로 부터 날라온 데이터를 적용하여 변경한다.

    # pk든 id 든 상관없음
    post = Post.objects.get(pk=pk)
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.img_url = request.GET.get('img_url')
    post.save()

    # <>에 들어있는건 콤마뒤에 따로 넣어줘야댐
    # return redirect('posts:detail', pk)
    return redirect(f'/posts/{pk}/')