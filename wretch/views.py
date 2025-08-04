from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def qa(request):
    return render(request, "qa.html")