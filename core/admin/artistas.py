from django.contrib import admin

from core.models import Artistas


class ArtistasAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)
admin.site.register(Artistas, ArtistasAdmin)
