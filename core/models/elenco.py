from django.db import models
from core.models.filmes import Filmes

from .artistas import Artistas

class Elenco(models.Model):
    personagem = models.CharField(max_length=50)
    nome = models.ForeignKey(Artistas, on_delete=models.PROTECT,related_name="Elenco")
    titulo = models.ManyToManyField(Filmes, related_name="Elenco")
    
    def __str__(self):
        return self.personagem