from django.db import models

from .genero import Genero
from .plataforma import Plataforma


class Filmes(models.Model):
    titulo = models.CharField(max_length=90)
    descricao = models.CharField(max_length=500)
    ano_lancamento = models.DateField()
    duracao = models.DurationField()
    produtor = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45)
    nome_genero = models.ManyToManyField(Genero, related_name="Filmes")
    streaming = models.ManyToManyField(Plataforma, related_name="Filmes")

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural="Filmes"