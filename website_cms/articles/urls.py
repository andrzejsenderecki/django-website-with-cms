from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^articles_all/$', views.articles_all, name='articles_all'),
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
]