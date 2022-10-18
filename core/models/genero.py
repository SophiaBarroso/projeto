from django.db import models


class Genero(models.Model):
    nome_genero = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nome_genero
    class Meta:
        verbose_name_plural = "Gêneros"