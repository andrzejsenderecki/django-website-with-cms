from django.shortcuts import render
from .models import Article

def articles_all(request):
    return render(request, 'articles/articles_all.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render(request, 'articles/article.html', {'article': Article.objects.get(id=article_id)})
