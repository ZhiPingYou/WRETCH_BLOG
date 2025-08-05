from django.urls import path
# from django.contrib import admin
from . import views





urlpatterns = [
    path("about/", views.about),
    path("", views.home),
    path("contact/", views.contact),
    
]