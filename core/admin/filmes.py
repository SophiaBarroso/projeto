from django.contrib import admin

from core.models import Filmes


class FilmesAdmin (admin.ModelAdmin):
    list_display = ("titulo", "classificacao", "ano_lancamento", "duracao")
    search_fields = ("titulo",)
admin.site.register(Filmes, FilmesAdmin)