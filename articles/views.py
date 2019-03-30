from django.shortcuts import render
from articles.models import Article, Comment
from .forms import CommentForm
from django.template.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def all_articles(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})

def single_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article.html", {"article": article})
    
def add_comment(request, article_id):
    art = Article.objects.get(id=article_id)
    if request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.published = timezone.now()
            comment.article = art
            comment.save()
            
            return HttpResponseRedirect('/article/%s' % article_id)
    else:
        cf = CommentForm()
        
    args = {}
    args.update(csrf(request))
    args['article'] = art
    args['form'] = cf
    
    return render(request, 'add_comment.html', args)