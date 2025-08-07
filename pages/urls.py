from django.urls import path
# from django.contrib import admin
from . import views

from articles.views import  index



app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    # path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),

    # 以下是把detail頁改當成首頁
    path("",index, name="home")
    
]