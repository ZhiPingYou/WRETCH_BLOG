from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.all().order_by("-id")
        return render(request, "articles/index.html", {"articles_no": articles})

def new(request):
    return render(request, "articles/new.html")

def detail(request, id):
    # try:
    #     article = Article.objects.get(pk=id)
    # except:
    #     return HttpResponse("不好意思目前找不到")
    article = get_object_or_404(Article, pk=id)
    if request.POST:
        if request.POST["_method"] == 'patch':
            title = request.POST["title"]
            content = request.POST["content"]
            article.title = title
            article.content = content
            article.save()
            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)
            
        if request.POST["_method"] == 'delete':
            article.delete()
            messages.success(request, "刪除成功")
            return redirect("articles:index")
            
    else:
        return render(request, "articles/detail.html", {"article": article})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    # messages.success(request, "修改成功")
    return render(request, "articles/edit.html", {"article": article})
