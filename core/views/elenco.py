from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Elenco
from core.serializers import ElencoSerializer

class ElencoViewSet(ModelViewSet):
    queryset = Elenco.objects.all()
    serializer_class = ElencoSerializer