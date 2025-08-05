from django.shortcuts import render
def home(request):
    lottery_numbers = [1, 2, 4, 5, 7, 36] 
    return render(request, "pages/home.html", {"lucky": lottery_numbers})

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")