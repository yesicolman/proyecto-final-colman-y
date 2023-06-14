from django.urls import path
from MiApp import views

urlpatterns = [
    path('', views.inicio, name="index"),
    path('destinos/', views.destino, name="destinos"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('post/', views.posts, name="post"),
    path('form_contacto/', views.form_contacto, name="form_contacto"),
    path('agregar_destino/', views.agregar_destino, name="agregar_destino"),
    path('buscar_destino', views.buscar_destino, name="buscar_destino")
]