from django.contrib import admin

from core.models import Filmes, Genero, Usuario, Artistas

admin.site.register(Filmes)
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Artistas)