from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField()
    senha = models.CharField(max_length=15)
    dt_nasc = models.DateField()

class Filmes(models.Model):
    titulo = models.CharField(max_length=90)
    descricao = models.CharField(max_length=500)
    ano_lancamento = models.DateField()
    duracao = models.DurationField()
    produtor = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45)

    def __str__(self):
        return self.titulo
    
class Genero(models.Model):
    nome_genero = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nome_genero
    
    class Meta:
        verbose_name_plural = "Generos"
        
class Artistas(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1500)
    
    def __str__(self):
        return self.nome
    
