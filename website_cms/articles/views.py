from django.shortcuts import render
from .models import Article, Comment
from .forms import CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect

def articles_all(request):
    return render(request, 'articles/articles_all.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render(request, 'articles/article.html', {'article': Article.objects.get(id=article_id)})

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