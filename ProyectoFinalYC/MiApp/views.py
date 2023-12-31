from django.shortcuts import render
from MiApp.models import Destino, Usuarios, Post, Guias, Comentario, Respuesta
from MiApp.forms import FormContacto, AgregarGuia, AgregarComentario, BuscaDestinoEnGuia
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from django.shortcuts import redirect

def inicio(request):
    try:
        url= Account.objects.filter(id=request.user.id)[0]
    except IndexError:
        url= None
    return render(request, "MiApp/baseweb.html", {url: url})

def about(request):
    return render(request, "MiApp/about.html")

# PARA ACCEDER AL TEMPLATE ORIGINAL BOOTSTRAP:

def index(request):
    return render(request, "MiApp/index.html")

#FORMULARIOS

def form_contacto(Request):

    if Request.method == "POST":
            miFormulario= FormContacto(Request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                 informacion = miFormulario.cleaned_data
                 nombre= Usuarios(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],mensaje=informacion["mensaje"])
                 nombre.save()
                 return render(Request, "MiApp/form_contacto_enviado.html")
    else:
         miFormulario= FormContacto()

    return render(Request, "MiApp/form_contacto.html", {"miFormulario": miFormulario})

def form_enviado(request):
    return render(request, "MiApp/form_contacto_enviado.html")

def agregar_comentario(Request):

    if Request.method == "POST":
            miComent= AgregarComentario(Request.POST)
            print(miComent)

            if miComent.is_valid():
                 informacion = miComent.cleaned_data
                 nombre= Comentario(usuario=informacion["usuario"],contenido=informacion["contenido"],fecha_publicacion=informacion["fecha_publicacion"])
                 nombre.save()
                 return render(Request, "MiApp/baseweb.html")
    else:
         miComent= AgregarComentario()

    return render(Request, "MiApp/agregar_comentario.html", {"miComent": miComent})

@login_required
def agregar_guia(Request):
    if Request.method == "POST":
            guia= AgregarGuia(Request.POST, Request.FILES)
            
            #if not Request.user.is_staff:
                #guia.fields['foto'].disabled = True
            
            print(guia)

            if guia.is_valid():
                informacion = guia.cleaned_data
                nombre= Guias(
                    #autor=informacion["autor"],
                    autor=Request.user,
                    titulo=informacion["titulo"],
                    subtitulo=informacion["subtitulo"],                    
                    destino=informacion["destino"],
                    pais=informacion["pais"],
                    foto=Request.FILES["foto"],
                    contenido=informacion["contenido"]
                )
                nombre.save()
                return redirect("Guias")
    else:
         guia= AgregarGuia()

    #return render(Request, "MiApp/agregar_guia.html", {"guia": guia})
    return render(Request, "MiApp/agregar_guia.html", {"guia": guia, 'request': Request})


def buscar_destino_enguia(request):
    if request.method == "POST":
        buscar_form = BuscaDestinoEnGuia(request.POST)

        if buscar_form.is_valid():
            info = buscar_form.cleaned_data
            guias = Guias.objects.filter(destino__icontains=info["destino"])
            return render(request, "MiApp/lista_guias_busqueda.html", {"guias": guias, 'request': request })
    else:
        buscar_form = BuscaDestinoEnGuia()
        return render(request, "MiApp/buscar_destino.html", {"buscar_form": buscar_form})