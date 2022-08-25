from django.contrib import admin

from core.models import Filmes, Genero, Usuario

admin.site.register(Filmes)
admin.site.register(Genero)
admin.site.register(Usuario)