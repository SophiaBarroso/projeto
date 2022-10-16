from django.db import models
from core.models.filmes import Filmes

from core.models.usuario import Usuario

class Critica(models.Model):
    estrelas = (
        (1, '1 estrelas'),
        (2, "2 estrelas"),
        (3, '3 estrelas'),
        (4, "4 estrelas"),
        (5, "5 estrelas"),
    )
    conteudo = models.CharField(max_length=500)
    dt_critica = models.DateField()
    crt_user = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='criticas')
    crt_filme = models.ForeignKey(Filmes, on_delete=models.PROTECT, related_name='criticas')
    nota = models.PositiveIntegerField(null=False, blank=True, choices=estrelas)
