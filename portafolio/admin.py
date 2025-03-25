from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Perfil, Certificado

admin.site.register(Perfil)
admin.site.register(Certificado)
