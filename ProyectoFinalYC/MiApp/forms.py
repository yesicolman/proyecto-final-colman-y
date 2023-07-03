from django import forms
from .models import Post


class FormContacto(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class AgregarDestino(forms.Form):

    nombre= forms.CharField()
    pais=forms.CharField()

class BuscaDestino(forms.Form):
    destino= forms.CharField()

class AgregarGuia(forms.Form):
    autor= forms.CharField()
    titulo = forms.CharField()
    destino= forms.CharField()
    pais = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea)

class AgregarComentario(forms.Form):
    usuario= forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=300, widget=forms.Textarea)
    fecha_publicacion = forms.DateTimeField()
