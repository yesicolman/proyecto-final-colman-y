from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView

from django.views.generic import DeleteView

from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

from accounts import forms
from accounts import models
from accounts.forms import UserEditForm
from accounts.forms import CambiarPass

# Para el registro se van a usar funciones:

def register(request):
    if request.method== 'POST':
        form = forms.RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/crear_cuenta.html', {'form':form})
        
    form= forms.RegistroUsuarioForm()
    return render(request, 'accounts/crear_cuenta.html', {'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "accounts/login.html", {"mensaje":"Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ = models.Account.objects.get_or_create(user=usuario)
    if request.method == "POST":
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')
            usuario.email = data.get('email') if data.get('email') else usuario.email
            modelo_perfil.avatar = data.get('avatar') if data.get('avatar') else modelo_perfil.avatar

            modelo_perfil.save()
            usuario.save()
            return redirect("mostrar_perfil")
        else:
            return render(request, 'accounts/editar_account.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, 'accounts/editar_cuenta.html', {'form': form})

def mostrar_perfil(request):
    return render(request, 'accounts/mostrar_cuenta.html')

def eliminar_perfil(request):
    ...

def cambiar_password(request):
    ...

class Logout(LogoutView):
    template_name= 'accounts/logout_account.html'

# Vista para editar el usuario

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        editForm = (request.POST)

        if editForm.is_valid():

            informacion = editForm.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return render(request, "MiApp/inicio.html")
    else:

        editForm = UserEditForm(initial={'email': usuario.email})
    return render(request, "accounts/editar_perfil.html", {"editForm": editForm, "usuario": usuario})


class CambiarPasswordView(LoginRequiredMixin, View):
    template_name = "accounts/cambiar_pass.html"
    form_class = CambiarPass
    success_url = reverse_lazy("Inicio")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        
        usuario = User.objects.get(id=request.user.id)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            pass1 = form.cleaned_data.get("password1")
            pass2 = form.cleaned_data.get("password2")
        
            if pass1 == pass2:
                usuario.set_password(pass1)
                usuario.save()
                return render(request, "MiApp/index.html")