from django.shortcuts import redirect, get_object_or_404
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages

# Create your views here.
def create(request, id):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=id)
        form = CommentForm(request.POST)

        comment = form.save(commit=False)
        comment.article = article
        comment.save()

        messages.success(request, "新增成功")
        return redirect("articles:detail", article.id)