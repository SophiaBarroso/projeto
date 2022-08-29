from rest_framework.serializers import ModelSerializer

from core.models import Filmes
from core.models import Genero

class FilmesSerializer(ModelSerializer):
    class Meta:
        model = Filmes
        fields = "__all__"
        
class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"