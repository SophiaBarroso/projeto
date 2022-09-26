from django.contrib import admin
from core.models import Plataforma

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("plataforma")

admin.site.register(Plataforma, PlataformaAdmin)
