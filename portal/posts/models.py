from django.db import models


class Noticia(models.Model):

    titulo = models.CharField('Título', max_length=100)
    conteudo = models.TextField('Conteúdo')
    data_publicacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_edicao = models.DateTimeField('Editado em', auto_now=True)

