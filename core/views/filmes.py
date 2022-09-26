from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Filmes
from core.serializers import FilmesSerializer

class FilmesViewSet(ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer