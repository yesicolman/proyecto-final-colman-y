from django.urls import path
from MiApp import views
from MiApp import class_views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('destinos/', views.destino, name="destinos"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('post/', views.posts, name="post"),
    path('form_contacto/', views.form_contacto, name="form_contacto"),
    path('agregar_destino/', views.agregar_destino, name="agregar_destino"),
    path('buscar_destino', views.buscar_destino, name="buscar_destino"),
    path('agregar_comentario', views.agregar_comentario, name="agregar_comentario"),
    path('agregar_guia', views.agregar_guia, name="agregar_guia"),
    path('about', views.about, name="about")
]


#--> + URLS Basadas en clases

urlpatterns += [
    path('list_post', class_views.PostListView.as_view(), name="List"),
    path('crear_post/', class_views.PostCreateView.as_view(), name="create"),
    path('detail_post/<pk>/', class_views.PostDetailView.as_view(), name="Detail"),
    path('update_post/<pk>/', class_views.PostUpdateView.as_view(), name="Update"),
    path('delete_post/<pk>/', class_views.PostDeleteView.as_view(), name="Delete"),
]