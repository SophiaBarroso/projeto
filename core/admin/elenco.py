from django.contrib import admin

from core.models import Elenco


class ElencoAdmin (admin.ModelAdmin):
    list_display = ("nome", "personagem")

admin.site.register(Elenco, ElencoAdmin)