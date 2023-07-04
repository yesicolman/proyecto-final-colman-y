from django.views.generic import ListView
from .models import Post, Guias, Comentario, Respuesta, Destino
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CRUD POST

class PostListView(ListView):

    model = Post
    template_name = "MiApp/class_list_post.html"

class PostDetailView(DetailView):

    model = Post
    template_name = "MiApp/class_detail_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foto'] = self.object.foto
        return context

class PostCreateView(CreateView):

    model = Post
    template_name = "MiApp/class_create_post.html"
    fields = ['titulo', 'subtitulo','autor','fecha_publicacion','foto','contenido']
    success_url = reverse_lazy("inicio")

class PostUpdateView(UpdateView):

    model = Post
    template_name= "MiApp/class_update_post.html"
    success_url = reverse_lazy("List")
    fields = ['titulo', 'subtitulo', 'autor', 'fecha_publicacion', 'contenido']
   
class PostDeleteView(DeleteView):

    model = Post
    success_url = reverse_lazy("List")
    template_name = "MiApp/class_confirm_delete_post.html"

# CRUD GUIA

class GuiaListView(ListView):

    model = Guias
    template_name = "MiApp/lista_guias.html"

class GuiaDetailView(DetailView):

    model = Guias
    template_name = "MiApp/class_detail_guias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foto'] = self.object.foto
        return context
    
class GuiaDeleteView(DeleteView):
    
    model = Guias
    success_url = reverse_lazy("Guias")
    template_name = "MiApp/class_confirm_delete_guia.html"