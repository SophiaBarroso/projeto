from django.db import models
        
from .filmes import Filmes

class Artistas(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1500)
    titulo = models.ManyToManyField(Filmes, related_name="Artistas")
    
    def __str__(self):
        return self.nome