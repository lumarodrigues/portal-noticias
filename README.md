# portal-noticias
Um CRUD em DRF para o jornal Abacate News

## Instalação Local

1. Clone o projeto

    ```bash
    git clone git@github.com:lumarodrigues/portal-noticias.git
    ```

2. Entre na pasta do projeto
    ```bash
    cd portal-noticias-backend/
    ```

3. Crie um arquivo **.env** com base no .env-sample.

    **IMPORTANTE:** Lembre de adicionar/alterar os valores nas variáveis do novo arquivo (.env)
    com os valores pertinentes.

    Exemplo:
    ```
    APP_PORT=8080
    DB_PORT=5678
    SECRET_KEY=string_aleatoria_gerada_pelo_django
    ```

4. Dê um build na imagem docker

    ```bash
    docker-compose build
    ```

5. Suba o banco de dados

    ```bash
    docker-compose up -d db
    ```

6. Execute as migrações

    ```bash
    docker-compose run --rm web python manage.py migrate
    ```

7. Para rodar a aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

## EXTRA

* Para rodar o linter

    ```bash
    docker-compose run --rm web flake8 .
    ```

* Para rodar os testes

    ```bash
    docker-compose run --rm web pytest
    ```

* Para subir o Redis para cache das notícias

    ```bash
    docker-compose up cache
    ```
