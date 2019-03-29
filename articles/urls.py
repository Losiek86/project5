from django.conf.urls import include, url
from .views import all_articles, single_article, add_comment

urlpatterns = [
    url(r'^show_all/$', all_articles, name = 'articles'),
    url(r'^(?P<article_id>\d+)/$', single_article, name = 'article'),
    url(r'^(?P<article_id>\d+)/add_comment/$', add_comment, name = 'comment'),
    ]