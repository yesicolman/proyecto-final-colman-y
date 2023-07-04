from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts= { key:'' for key in fields }


class EditarUsuarioForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name=forms.CharField(label= 'Nombre', max_length=30, required=False)
    Last_name=forms.CharField(label= 'Apellido', max_length=30, required=False)
    avatar= forms.ImageField(required=False)


class UserEditForm(UserCreationForm):
    email: forms.EmailField(label= "Ingrese su e-mail: ")
    password1: forms.CharField(label= "Ingresar contraseña: ", widget= forms.PasswordInput)
    password2: forms.CharField(label= "Reingresar contraseña: ",widget= forms.PasswordInput)
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User
        fields= ["email", "password1", "password2", "last_name", "first_name"]
    

class CambiarPass(forms.Form):

    password1 = forms.CharField(label="Ingresar Nueva contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Nueva contraseña", widget=forms.PasswordInput())