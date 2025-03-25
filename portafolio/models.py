from django.db import models

# Create your models here.
from django.db import models

class Perfil(models.Model):
    foto = models.ImageField(upload_to='foto_perfil/')
    cv = models.FileField(upload_to='cv/')

class Certificado(models.Model):
    imagen = models.ImageField(upload_to='certificados/')
