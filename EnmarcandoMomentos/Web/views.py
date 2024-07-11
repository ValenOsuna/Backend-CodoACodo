from django.shortcuts import render
from Noticias.models import Noticia

# Create your views here.

def about(request):
    return render(request, 'Web/about.html')

def contact(request):
    return render(request, 'Web/contact.html')

def user(request):
    return render(request, 'Web/user.html')

def register(request):
    return render(request, 'Web/register.html')

def index(request):
    Notas = Noticia.objects.all()
    Noticias = []
    for i in Notas:
        if len(Noticias) < 1:
            Noticias.append(i)
    return render(request, 'Web/index.html', {'Noticias': Noticias})

def mensaje(request):
    return render(request, 'Web/mensaje.html')