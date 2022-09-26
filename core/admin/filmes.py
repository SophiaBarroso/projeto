from django.contrib import admin
from core.models import Filmes

class FilmesAdmin (admin.ModelAdmin):
    list_display = ("titulo", "ano_lancamento", "duracao")

admin.site.register(Filmes, FilmesAdmin)