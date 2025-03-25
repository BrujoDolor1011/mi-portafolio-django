from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Perfil, Certificado

def home(request):
    perfil = Perfil.objects.first()  # Obtiene la primera foto de perfil y CV
    certificados = Certificado.objects.all()  # Obtiene TODOS los certificados
    return render(request, 'portafolio/home.html', {'perfil': perfil, 'certificados': certificados})
