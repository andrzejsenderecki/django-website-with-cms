from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home/$', views.articles_all, name='home'),
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^user_articles/$', views.article_user, name='user_articles'),
    url(r'^(?P<article_id>\d+)/user_article_edit/$', views.article_user_edit, name='user_article_edit'),
    url(r'^(?P<article_id>\d+)/edit_article/$', views.edit_article, name='edit_article'),
    url(r'^(?P<article_id>\d+)/new_comment/$', views.new_comment, name='new_comment'),
]