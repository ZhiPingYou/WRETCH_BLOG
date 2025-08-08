from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib import messages
from .forms import  ArticleForm
from comment.forms import CommentForm


def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        # title = request.POST.get['title']
        # content = request.POST.get['content']
        # is_published = request.POST.get["is_published"] == "on"
        # Article.objects.create(title=title, content=content)
        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.all().order_by("-id")
        # articles = Article.objects.filter(is_published=True).order_by("-id")
        return render(request, "articles/index.html", {"articles_no": articles})

def new(request):
    form = ArticleForm()
    return render(request, "articles/new.html", {"form": form})

def detail(request, id):
    # try:
    #     article = Article.objects.get(pk=id)
    # except:
    #     return HttpResponse("不好意思目前找不到")
    article = get_object_or_404(Article, pk=id)
    if request.POST:
        if request.POST.get("_method") == 'patch':
            form = ArticleForm(request.POST, instance=article)
            form.save()
            # title = request.POST.get["title"]
            # content = request.POST.get["content"]
            # article.is_published = request.POST["is_published"] == "on"
            # article.title = title
            # article.content = content
            # article.save()
            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)
            
        if request.POST["_method"] == 'delete':
            article.delete()
            messages.success(request, "刪除成功")
            return redirect("articles:index")
            
    else:
        comment_form = CommentForm()
        comments = article.comment_set.order_by("-id")

        return render(request, "articles/detail.html", {"article": article}, {"comment_form": comment_form}, {"comments": comments})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(instance= Article)
    # messages.success(request, "修改成功")
    return render(request, "articles/edit.html", {"article": article, "form": form})
