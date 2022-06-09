from portal.posts.models import Noticia


def test_escrever_noticia(client):
    response = client.post(
        '/api/noticias/',
        data={
            'titulo': 'Título 1',
            'conteudo': 'Conteudo 1',
            'data_publicacao': '2022-06-05T21:33:41.084376-03:00',
            'data_edicao': '2022-06-05T21:33:41.084376-03:00',
        },
        format='json'
    )
    assert Noticia.objects.count() == 1
    assert response.status_code == 201


def test_ver_noticia(client, noticia):
    response = client.get(
        f'/api/noticias/{noticia.id}/',
        data={},
        format='json'
    )
    assert response.status_code == 200


def test_editar_noticia(client, noticia):
    titulo_antigo = noticia.titulo
    response = client.put(
        f'/api/noticias/{noticia.id}/',
        data={
            'titulo': 'Título Novo',
            'conteudo': 'Conteudo Teste'
        },
        format='json'
    )
    noticia.refresh_from_db()
    assert titulo_antigo != noticia.titulo
    assert response.status_code == 200


def test_excluir_noticia(client, noticia):
    response = client.delete(
        f'/api/noticias/{noticia.id}/',
        data={},
        format='json'
    )
    assert response.status_code == 204
