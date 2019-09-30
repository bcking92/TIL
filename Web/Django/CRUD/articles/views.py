from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    context = {

    }
    return render(request, 'new.html', context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    img_url = request.GET.get('img_url')
    Article(title = title, content = content, img_url = img_url).save()

    return redirect('index')

def index(request):
    context = {
        'Article' : reversed(Article.objects.all()),
    }
    return render(request, 'index.html', context)

def post(request,num):
    num = num
    context = {
        'post' : Article.objects.filter(id=num)[0],
    }
    return render(request, 'post.html', context)
