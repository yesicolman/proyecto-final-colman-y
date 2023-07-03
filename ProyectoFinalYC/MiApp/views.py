from django.shortcuts import render
from MiApp.models import Destino, Usuarios, Post, Guias, Comentario, Respuesta
from MiApp.forms import FormContacto, AgregarDestino,BuscaDestino, AgregarGuia, AgregarComentario

from accounts.models import Account

def inicio(request):
    try:
        url= Account.objects.filter(id=request.user.id)[0]
    except IndexError:
        url= None
    return render(request, "MiApp/baseweb.html", {url: url})

def destino(request):
    return render(request, "MiApp/destinos.html")

def usuarios(request):
    return render(request, "MiApp/usuarios.html")

def posts(request):
    return render(request, "MiApp/post.html")

def about(request):
    return render(request, "MiApp/about.html")

#FORMULARIOS

def form_contacto(Request):

    if Request.method == "POST":
            miFormulario= FormContacto(Request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                 informacion = miFormulario.cleaned_data
                 nombre= Usuarios(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
                 nombre.save()
                 return render(Request, "MiApp/index.html")
    else:
         miFormulario= FormContacto()

    return render(Request, "MiApp/form_contacto.html", {"miFormulario": miFormulario})

def agregar_destino(Request):

    if Request.method == "POST":
            miFormulario= AgregarDestino(Request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                 informacion = miFormulario.cleaned_data
                 nombre= Destino(nombre=informacion["nombre"], pais=informacion["pais"])
                 nombre.save()
                 return render(Request, "MiApp/index.html")
    else:
         miFormulario= AgregarDestino()

    return render(Request, "MiApp/agregar_destino.html", {"miFormulario": miFormulario})

def buscar_destino(request):
    if request.method == "POST":
        buscar_destino = BuscaDestino(request.POST)

        if buscar_destino.is_valid():
            info = buscar_destino.cleaned_data
            destino = Destino.objects.filter(nombre__icontains=info["destino"])
            return render(request,"MiApp/lista_destino.html", {"destino": destino})
    else:
        buscar_destino = BuscaDestino()
        return render(request, "MiApp/buscar_destino.html", {"miFormulario": buscar_destino})


def agregar_comentario(Request):

    if Request.method == "POST":
            miComent= AgregarComentario(Request.POST)
            print(miComent)

            if miComent.is_valid():
                 informacion = miComent.cleaned_data
                 nombre= Comentario(usuario=informacion["usuario"],contenido=informacion["contenido"],fecha_publicacion=informacion["fecha_publicacion"])
                 nombre.save()
                 return render(Request, "MiApp/index.html")
    else:
         miComent= AgregarComentario()

    return render(Request, "MiApp/agregar_comentario.html", {"miComent": miComent})


def agregar_guia(Request):

    if Request.method == "POST":
            guia= AgregarGuia(Request.POST)
            print(guia)

            if guia.is_valid():
                 informacion = guia.cleaned_data
                 nombre= Guias(autor=informacion["autor"], titulo=informacion["titulo"], destino=informacion["destino"],pais=informacion["pais"],contenido=["Contenido"])
                 nombre.save()
                 return render(Request, "MiApp/index.html")
    else:
         guia= AgregarGuia()

    return render(Request, "MiApp/agregar_guia.html", {"guia": guia})

