from rest_framework.serializers import ModelSerializer

from core.models import Critica

class CriticaSerializer(ModelSerializer):
    class Meta:
        model = Critica
        fields = "__all__"
        