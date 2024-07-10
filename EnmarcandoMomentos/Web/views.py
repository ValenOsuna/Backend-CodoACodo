from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Web/index.html')

def about(request):
    return render(request, 'Web/about.html')

def contact(request):
    return render(request, 'Web/contact.html')

def user(request):
    return render(request, 'Web/user.html')

def register(request):
    return render(request, 'Web/register.html')