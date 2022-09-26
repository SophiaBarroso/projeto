from django.contrib import admin
from core.models import Genero

class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome_genero",)

admin.site.register(Genero, GeneroAdmin)