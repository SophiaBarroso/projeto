from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Filmes, Genero
from core.serializers import FilmesSerializer, GeneroSerializer

class FilmesViewSet(ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    
class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
