from django.shortcuts import render
from .models import Causa  # Asumiendo que tu modelo se llama Causa
# Create your views here.


def Donar(request):
    causas = Causa.objects.all()
    return render(request, 'Causas/donaciones.html', {'causas': causas})
