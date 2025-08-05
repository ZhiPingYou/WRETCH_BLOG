from django.shortcuts import render, redirect
from .models import Article


def index(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect("articles:index")
    else:
        articles = Article.objects.all().order_by("-id")
        return render(request, "articles/index.html", {"articles_no": articles})

def new(request):
    return render(request, "articles/new.html")

def detail(request, id):
    return render(request, "articles/detail.html", {"id": id})
