from rest_framework.serializers import ModelSerializer

from core.models import Plataforma


class PlataformaSerializer(ModelSerializer):
    class Meta:
        model = Plataforma
        fields = "__all__"
