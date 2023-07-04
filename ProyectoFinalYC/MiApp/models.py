from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)


class Usuarios(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    mensaje= models.CharField(max_length=500,null=False,default="mensaje no encontrado")

class Post(models.Model):

    titulo = models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=80, default="")
    autor = models.CharField(max_length=20, default='unknown_user')
    fecha_publicacion = models.DateTimeField()
    foto= models.ImageField(upload_to='fotos/',null=True, blank=True)
    contenido = models.TextField(max_length=1000)
    

class Guias(models.Model):

    autor= models.CharField(max_length=20)
    titulo = models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=80, default="")
    destino= models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    foto= models.ImageField(upload_to='fotos/',null=True, blank=True)
    contenido = models.TextField(max_length=1000)

class Comentario(models.Model):
    usuario= models.CharField(max_length=40)
    contenido = models.CharField(max_length=300)
    fecha_publicacion = models.DateTimeField()
    
class Respuesta(models.Model):
    usuario= models.CharField(max_length=40)
    contenido = models.TextField(max_length=200)
    fecha_publicacion = models.DateTimeField()

