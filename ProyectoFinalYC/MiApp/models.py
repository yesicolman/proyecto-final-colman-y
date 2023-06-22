from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)


class Usuarios(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Post(models.Model):

    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=300)
    fecha_publicacion = models.DateTimeField()

class Guias(models.Model):

    autor= models.CharField(max_length=20)
    titulo = models.CharField(max_length=40)
    destino= models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    contenido = models.CharField(max_length=1000)

class Comentario(models.Model):
    usuario= models.CharField(max_length=40)
    contenido = models.CharField(max_length=300)
    fecha_publicacion = models.DateTimeField()
    
class Respuesta(models.Model):
    usuario= models.CharField(max_length=40)
    contenido = models.CharField(max_length=300)
    fecha_publicacion = models.DateTimeField()

# Create your models here.
