from django.db import models
        
class Plataforma(models.Model):
    plataforma = models.CharField(max_length=20)

    def __str__(self):
        return self.plataforma
