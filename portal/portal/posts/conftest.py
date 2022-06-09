import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def noticia(db):
    return baker.make(
        'posts.Noticia',
        titulo='Noticia Teste',
        conteudo='Conteudo Teste',
        data_publicacao='2022-06-05T21:33:41.084376-03:00',
        data_edicao='2022-06-05T22:40:32.084300-03:00',
    )


@pytest.fixture
def client(db):
    return APIClient()
