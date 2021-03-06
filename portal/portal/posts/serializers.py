from rest_framework import serializers
from portal.posts.models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticia
        fields = (
            'id',
            'titulo',
            'conteudo',
            'data_publicacao',
            'data_edicao'
        )
