from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import FilmesViewSet, GeneroViewSet, ArtistasViewSet, PlataformaViewSet, CriticaViewSet

router = DefaultRouter()
router.register(r'filmes', FilmesViewSet)
router.register(r'genero', GeneroViewSet)
router.register(r'artistas', ArtistasViewSet)
router.register(r'plataforma', PlataformaViewSet)
router.register(r'critica', CriticaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]