from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^articles_all/$', views.articles_all, name='articles_all'),
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^(?P<article_id>\d+)/new_comment/$', views.new_comment, name='new_comment'),
]