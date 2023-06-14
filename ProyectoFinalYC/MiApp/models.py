from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)


class Usuarios(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Post(models.Model):

    Titulo = models.CharField(max_length=40)
    Contenido = models.CharField(max_length=300)
    fecha_publicacion = models.DateTimeField()
    
# Create your models here.
