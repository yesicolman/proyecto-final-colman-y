from django.contrib import admin
from .models import Usuarios, Post, Destino, Guias, Comentario, Respuesta


# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Destino)
admin.site.register(Comentario)
admin.site.register(Respuesta)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('foto',)
        return self.readonly_fields

@admin.register(Guias)
class GuiasAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('foto',)
        return self.readonly_fields