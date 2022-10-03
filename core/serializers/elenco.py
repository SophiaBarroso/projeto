from rest_framework.serializers import ModelSerializer

from core.models import Elenco

class ElencoSerializer(ModelSerializer):
    class Meta:
        model = Elenco   
        fields = "__all__"