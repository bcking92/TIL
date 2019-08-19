from django.shortcuts import render, redirect
from datetime import datetime
from .models import Article

contents = []

# class Articles:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at
#     def __str__(self):
#         return f'제목 : {self.title}, 내용 : {self.content}, 시간 : {self.created_at}'

def new(request):
    context = {

    }
    return render(request, 'new.html', context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    img_url = request.GET.get('img_url')
    Article(title = title, content = content, img_url = img_url).save()
    # now = datetime.now
    contents.append(Article(title = title,content = content))

    # return render(request, 'create.html', context)
    return redirect('index')

def index(request):
    articles = reversed(Article.objects.all())
    context = {
        'contents' : contents,
        'articles' : articles,
    }
    return render(request, 'index.html', context)