from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = Article.objects.get(id=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        # form아 request.POST에 있는 data 니가 알아서좀 집어넣어라
        form = ArticleForm(request.POST)
        
        # 전송된 데이터가 유효한 값인지 검사하기
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(
                title=title,
                content=content,
            )
            return redirect(article)
        else:
            return redirect('create')
    else:
        # input 태그까지 만들어주는 코드임
        form = ArticleForm()
        print('----')
        print(form)
        print('----')
        context = {
            'form' : form,
        }
        return render(request, 'articles/create.html', context)

    