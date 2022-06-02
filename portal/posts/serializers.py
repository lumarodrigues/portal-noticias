from rest_framework import serializers 
from posts.models import Noticia
 
 
class NoticiaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Noticia
        fields = ('titulo',
                  'conteudo',
                  'data_publicacao',
                  'data_edicao')
