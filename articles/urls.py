from django.urls import path
# from django.contrib import admin
from . import views



app_name = "articles"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("new/", views.new, name="new"),
    
]