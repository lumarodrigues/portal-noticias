from .viewsets import NoticiaViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'noticias', NoticiaViewSet, basename='noticias')
urlpatterns = router.urls
