from django.urls import path
from django.shortcuts import render
from django.contrib import admin


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def qa(request):
    return render(request, "qa.html")


urlpatterns = [
    path("about/", about),
    path("", home),
    path("qa/", qa),
    path ("admin/", admin.site.urls)
]
