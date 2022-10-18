from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Critica
from core.serializers import CriticaSerializer


class CriticaViewSet(ModelViewSet):
    queryset = Critica.objects.all()
    serializer_class = CriticaSerializer