from django.db import models

class Filmes(models.Model):
    titulo = models.CharField(max_length=90)
    descricao = models.CharField(max_length=500)
    ano_lancamento = models.DateField()
    duracao = models.IntegerField()
    produtor = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45)

    def __str__(self):
        return self.titulo
    
class Genero(models.Model):
    nome_genero = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nome_genero