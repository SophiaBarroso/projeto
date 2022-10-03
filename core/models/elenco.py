from django.db import models
from core.models.elenco import Elenco

from .artistas import Artistas

class Elenco(models.Model):
    personagem = models.CharField(max_length=50)
    nome = models.ForeignKey(Artistas, related_name="Elenco")
    titulo = models.ManyToManyField(Filmes, related_name="Artistas")
    
    def __str__(self):
        return self.personagem