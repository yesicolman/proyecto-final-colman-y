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

#REGISTRO DE UN NUEVO USUARIO: 

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

#LOGIN DE UN USUARIO EXISTENTE:

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

#EDITAR PERFIL DE USUARIO EXISTENTE Y AGREGAR AVATAR:

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
            return render(request, 'accounts/editar_perfil.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, 'accounts/editar_perfil.html', {'form': form})

# MOSTRAR CUENTA:

def mostrar_cuenta(request):
    return render(request, 'accounts/mostrar_cuenta.html')

# LOG OUT:

class Logout(LogoutView):
    template_name= 'accounts/logout_account.html'

# CAMBIAR PASS:

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
                return render(request, "accounts/login.html")