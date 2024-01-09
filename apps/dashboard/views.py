from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def profile(request):
    return render(request, 'pages/profile.html')

def sign_in(request):
    return render(request, 'pages/sign-in.html')

def sign_up(request):
    return render(request, 'pages/sign-up.html')