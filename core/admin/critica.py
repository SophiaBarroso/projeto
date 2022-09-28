from django.contrib import admin
from core.models import Critica

class CriticaAdmin(admin.ModelAdmin):
    list_display = ("conteudo", "crt_user", "crt_filme", "nota")

admin.site.register(Critica, CriticaAdmin)