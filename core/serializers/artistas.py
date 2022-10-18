from rest_framework.serializers import ModelSerializer

from core.models import Artistas


class ArtistasSerializer(ModelSerializer):
    class Meta:
        model = Artistas   
        fields = "__all__"
