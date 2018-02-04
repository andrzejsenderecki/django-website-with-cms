from django.shortcuts import render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def articles_all(request):
    return render(request, 'articles/articles_all.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render(request, 'articles/article.html', {'article': Article.objects.get(id=article_id)})

@login_required
def new_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.published = timezone.now()
            new_article.save()
            return HttpResponseRedirect('/article/articles_all')
    else:
        article_form = ArticleForm()
    return render(request, 'articles/new_article.html', {'article_form': article_form})

def new_comment(request, article_id):
    article_number = Article.objects.get(id=article_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.published = timezone.now()
            comment.article = article_number
            comment.save()
            return HttpResponseRedirect('/article/%s' % article_id)
    else:
        comment_form = CommentForm()
    return render(request, 'articles/new_comment.html', {'comment_form': comment_form})

