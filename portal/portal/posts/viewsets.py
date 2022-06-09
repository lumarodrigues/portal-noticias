from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Noticia
from .serializers import NoticiaSerializer
# from portal.settings import CACHE_TTL


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

    @method_decorator(cache_page(60*60))
    def list(self, request):
        return super().list(request)

    @method_decorator(cache_page(60*60))
    def create(self, request):
        return super().create(request)

    @method_decorator(cache_page(60*60))
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=None)

    @method_decorator(cache_page(60*60))
    def update(self, request, pk=None):
        return super().update(request, pk=None)

    @method_decorator(cache_page(60*60))
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=None)

    @method_decorator(cache_page(60*60))
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=None)
