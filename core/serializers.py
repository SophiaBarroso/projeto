from rest_framework.serializers import ModelSerializer

from core.models import Filmes
from core.models import Genero
from core.models import Plataforma
from core.models import Artistas
from core.models import Usuario

class FilmesSerializer(ModelSerializer):
    class Meta:
        model = Filmes
        fields = "__all__"
        
class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"

class PlataformaSerializer(ModelSerializer):
    class Meta:
        model = Plataforma
        fields = "__all__"

class ArtistasSerializer(ModelSerializer):
    class Meta:
        model = Artistas   
        fields = "__all__"

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"