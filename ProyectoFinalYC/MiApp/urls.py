from django.urls import path
from MiApp import views
from MiApp import class_views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('form_contacto/', views.form_contacto, name="form_contacto"),
    path('form_contacto_ok/', views.form_enviado, name="form_contacto_ok"),
    path('buscar_destino', views.buscar_destino_enguia, name="buscar_destino"),
    path('agregar_comentario', views.agregar_comentario, name="agregar_comentario"),
    path('agregar_guia', views.agregar_guia, name="agregar_guia"),
]


#--> + URLS Basadas en clases

urlpatterns += [
    #--> CRUD POST
    path('list_post', class_views.PostListView.as_view(), name="List"),
    path('crear_post/', class_views.PostCreateView.as_view(), name="create"),
    path('detail_post/<pk>/', class_views.PostDetailView.as_view(), name="Detail"),
    path('update_post/<pk>/', class_views.PostUpdateView.as_view(), name="Update"),
    path('delete_post/<pk>/', class_views.PostDeleteView.as_view(), name="Delete"),

    #--> GUIAS
    path('guias/', class_views.GuiaListView.as_view(), name="Guias"),
    path('detail_guia/<pk>/', class_views.GuiaDetailView.as_view(), name="Detail_Guia"),
    path('borrar_guia/<pk>/', class_views.GuiaDeleteView.as_view(), name="Delete_Guia")
]