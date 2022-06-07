from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Noticia
from .serializers import NoticiaSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/noticia/pk/delete'
    }
  
    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    noticia = NoticiaSerializer(data=request.data)

    # if Noticia.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('Esta notícia já existe.')
  
    if noticia.is_valid():
        noticia.save()
        return Response(noticia.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):

    if request.query_params:
        noticias = Noticia.objects.filter(**request.query_param.dict())
    else:
        noticias = Noticia.objects.all()

    if noticias:
        data = NoticiaSerializer(noticias)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    data = NoticiaSerializer(instance=noticia, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
