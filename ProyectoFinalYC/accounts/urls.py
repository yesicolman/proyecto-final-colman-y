from django.urls import path
from accounts import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('perfil/', views.mostrar_cuenta, name='mostrar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('cambiar_pass/', views.CambiarPasswordView.as_view(), name="cambiar_pass"),
]