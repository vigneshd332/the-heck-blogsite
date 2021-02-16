from django.shortcuts import render, redirect
from django.http import HttpResponse as HR
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articlelist.html', {'articles' : articles})

def article_details(request, slug):
    #return HR(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/articledetails.html', {'article' : article} )

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticle()
    return render(request, 'articles/article_create.html',{'form':form})     