from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Filmes, Genero, Artistas, Usuario, Plataforma
from core.serializers import FilmesSerializer, GeneroSerializer, ArtistasSerializer, UsuarioSerializer, PlataformaSerializer

class FilmesViewSet(ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    
class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class ArtistasViewSet(ModelViewSet):
    queryset = Artistas.objects.all()
    serializer_class = ArtistasSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PlataformaViewSet(ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer
