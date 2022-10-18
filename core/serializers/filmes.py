from rest_framework.serializers import ModelSerializer

from core.models import Filmes


class FilmesSerializer(ModelSerializer):
    class Meta:
        model = Filmes
        fields = "__all__"
        