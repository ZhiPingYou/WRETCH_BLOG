from django.db import models
from articles.models import Article

# Create your models here.

class Comment(models.Model):
    content = models.TextField(null=False)
    # 以下是建立外部key(因為留言並非單一)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    # 建立時間
    created_at = models.DateTimeField(auto_now_add=True)
    # soft delete假刪
    # is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, db_index=True)
    #加索引 index增加效率