from django.shortcuts import render
from .models import Noticia

# Create your views here.

def Deporte(request):
    Noticias= Noticia.objects.filter(sector = "Deporte")
    return render(request, 'Noticias/Noticias.html', {'Noticias': Noticias})

def Salud(request):
    Noticias= Noticia.objects.filter(sector = "Salud")
    return render(request, 'Noticias/Noticias.html', {'Noticias': Noticias})

def Negocios(request):
    Noticias= Noticia.objects.filter(sector = "Negocios")
    return render(request, 'Noticias/Noticias.html', {'Noticias': Noticias})

def Mundo(request):
    Noticias= Noticia.objects.filter(sector = "Mundo")
    return render(request, 'Noticias/Noticias.html', {'Noticias': Noticias})