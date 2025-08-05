from django.urls import path
# from django.contrib import admin
from . import views



app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<int:id>/", views.detail, name="detail"),
    # 除首頁""外, 其它最好加斜線
]