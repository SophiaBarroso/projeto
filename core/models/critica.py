from django.db import models
from core.models.filmes import Filmes

from core.models.usuario import Usuario

class Critica(models.Model):
    conteudo = models.CharField(max_length=125)
    dt_critica = models.DateField()
    crt_user = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='criticas')
    crt_filme = models.ForeignKey(Filmes, on_delete=models.PROTECT, related_name='criticas')
