from django.shortcuts import render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def articles_all(request):
    return render(request, 'articles/articles_all.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render(request, 'articles/article.html', {'article': Article.objects.get(id=article_id)})

@login_required
def article_user(request):
    current_user = User.objects.get(username=request.user)
    articles_user = Article.objects.filter(author__username=current_user)
    return render(request, 'articles/articles_user.html', {'articles_user': articles_user, 'current_user': current_user})

@login_required
def article_user_edit(request, article_id):
    current_user = User.objects.get(username=request.user)
    articles_user = Article.objects.filter(author__username=current_user)
    return render(request, 'articles/articles_user_edit.html', {'articles_user': articles_user, 'article': Article.objects.get(id=article_id), 'current_user': current_user})

@login_required
def new_article(request):
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = request.user
            new_article.published = timezone.now()
            new_article.save()
            return HttpResponseRedirect('/dashboard')
    else:
        article_form = ArticleForm()
    return render(request, 'articles/new_article.html', {'article_form': article_form, 'current_user': current_user})

@login_required
def edit_article(request, article_id):
    current_user = User.objects.get(username=request.user)
    edit_article = Article.objects.get(id=article_id)
    edit_article_form = ArticleForm(initial={'title': edit_article.title, 'content': edit_article.content,
                                                 'image': edit_article.image})
    if request.method == 'POST':
        edit_article = Article.objects.get(id=article_id)
        edit_article_form = ArticleForm(instance=edit_article, data=request.POST, files = request.FILES,
                                            initial={'title': edit_article.title, 'content': edit_article.content,
                                                     'image': edit_article.image})
        if edit_article_form.is_valid():
            new_article = edit_article_form.save(commit=False)
            new_article.author = request.user
            new_article.published = timezone.now()
            new_article.save()
            return HttpResponseRedirect('/dashboard')
        else:
            edit_article = ArticleForm()
    return render(request, 'articles/edit_article.html', {'edit_article_form': edit_article_form, 'current_user': current_user})

def new_comment(request, article_id):
    article_number = Article.objects.get(id=article_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.published = timezone.now()
            comment.article = article_number
            comment.save()
            return HttpResponseRedirect('/%s' % article_id)
    else:
        comment_form = CommentForm()
    return render(request, 'articles/new_comment.html', {'comment_form': comment_form})