from django.urls import path
from django.contrib import admin
from .views import about, home, qa





urlpatterns = [
    path("about/", about),
    path("", home),
    path("qa/", qa),
    path ("admin/", admin.site.urls)
]
