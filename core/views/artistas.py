from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Artistas
from core.serializers import ArtistasSerializer


class ArtistasViewSet(ModelViewSet):
    queryset = Artistas.objects.all()
    serializer_class = ArtistasSerializer
   
