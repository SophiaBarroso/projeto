from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import FilmesViewSet, GeneroViewSet, ArtistasViewSet, PlataformaViewSet

router = DefaultRouter()
router.register(r'filmes', FilmesViewSet)
router.register(r'genero', GeneroViewSet)
router.register(r'artistas', ArtistasViewSet)
router.register(r'plataforma', PlataformaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]