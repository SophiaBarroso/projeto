from django.contrib import admin
from core.models import Elenco

class ElencoAdmin (admin.ModelAdmin):
    list_display = ("artista", "personagem")

admin.site.register(Elenco, ElencoAdmin)