from django.urls import path
# from django.contrib import admin
from . import views
from comments import views as comment_views



app_name = "articles"


# 除首頁""外, 其它最好加斜線
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<int:id>/", views.detail, name="detail"),

    # 以下是新增編輯頁
    path("<int:id>/edit/", views.edit, name="edit"),

    path("<int:id>/comments", comment_views.detail, name="create_comment"),

    
]