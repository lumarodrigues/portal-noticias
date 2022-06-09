from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Noticia
from .serializers import NoticiaSerializer
from portal.settings import CACHE_TTL


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request):
        print('abacate')  # Somente printa no primeiro carregamento, por conta do cache
        return super().list(request)

    def create(self, request):
        cache.clear()
        return super().create(request)

    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, pk=None):
        print('abacate')  # Somente printa no primeiro carregamento, por conta do cache
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        cache.clear()
        return super().update(request, pk=pk)

    def partial_update(self, request, pk=None):
        cache.clear()
        return super().partial_update(request, pk=pk)

    def destroy(self, request, pk=None):
        cache.clear()
        return super().destroy(request, pk=pk)
