from django.views.generic import ListView
from .models import Post, Guias, Comentario, Respuesta
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Listar para mostrar todos
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

