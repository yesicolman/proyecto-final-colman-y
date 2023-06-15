from django import forms


class FormContacto(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class AgregarDestino(forms.Form):

    nombre= forms.CharField()
    pais=forms.CharField()

class BuscaDestino(forms.Form):
    destino= forms.CharField()