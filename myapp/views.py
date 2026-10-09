from django.shortcuts import render, redirect

def login_view(request):
    return render(request, 'myapp/login.html')

def index(request):
    return render(request, 'myapp/index.html')