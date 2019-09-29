from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")

def signup_page(request):
    return render(request, "signup.html")

def login_page(request):
    return render(request, "login.html")

def logout_page(request):
    return render(request, "logout.html")

def contact_page(request):
    return render(request, "home.html")