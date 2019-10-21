from django.shortcuts import render, redirect, get_object_or_404, Http404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.views.decorators.http import require_POST
# from django.http import Http404

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    # if not Article.objects.get(pk=article_pk)
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except Article.DoesNotExist:
    #     raise Http404('해당하는 id의 글이 존재하지 않습니다.')
    comments = article.comment_set.all()
    # embed()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        # form아 request.POST에 있는 data 니가 알아서좀 집어넣어라
        form = ArticleForm(request.POST)
        # embed()
        # 전송된 데이터가 유효한 값인지 검사하기
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(
            #     title=title,
            #     content=content,
            # )
            article = form.save()
            return redirect(article)
        else:
            return redirect('create')
    else:
        # input 태그까지 만들어주는 코드임
        form = ArticleForm()
        comment_form = CommentForm()
        context = {
            'form': form,
            'comment_form': comment_form,
            
        }
        return render(request, 'articles/create.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, id=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article.title = title
            # article.content = content
            # article.save()
            form.save()
            return redirect(article)
    # embed()
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_POST
def delete(reqeust, article_pk):
    article = get_object_or_404(Article, id=article_pk)
    if reqeust.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')
    
@require_POST
def comments(request, article_pk):
    article = get_object_or_404(Article, id=article_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        # embed()
        if comment_form.is_valid():
            temp = comment_form.save(commit=False)
            temp.article = article
            temp.save()
            # return redirect('articles:detail', article_pk)
            return redirect(article)
    return redirect(article)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, id=article_pk)
    if request.method == "POST":
        Comment.objects.get(id=comment_pk).delete()
        return redirect(article)
    
    return redirect(article)