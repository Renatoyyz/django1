# Projeto django

Para criar projeto django.

```text
django-admin startproject <nome-projeto> .
O ponto no final é para criar o projeto no diretório atual. Sem o ponto, ele cria um dirtório raiz e o projeto dentro.
```

Para criar a aplicação

```text
django-admin startapp <nome-aplicacao>
```

 Para cada aplicação criada tem que por no settings do projeto

 No arquivo settings, colocar o diretório onde vão estar os templates

Para rodar uma aplicação

 ```text
 python manage.py runserver
 ```

Para gerar os modelos do banco de dados

```text
python manage.py makemigrations
```

Para criar as tabelas no banco de dados

```text
python manage.py migrate
```

Para criar usuário de admin (usuário e senha só para teste)

```text
python manage.py createsuperuser
usuário: renato
senha: renato123
```

Definir os paths para os arquivos estáticos no arquivo settings.py:

```text
STATIC_URL = 'static/' # Usado no desenvolvimento
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Usado na produção
```

Para redirecionar quando deslogar

```text
LOGIN_REDIRECT_URL = '/'
```

Para subir um projeto para web

```text
1 - Por o DEBUG = False no arquivo settings.py

2 - No ALLOWED_HOSTS = ['*'] por o servidor onde vai rodar
    se for em servidor gratuito para testes, deixar  ALLOWED_HOSTS = ['*'], se não por o dominio como:
    ALLOWED_HOSTS = ['meudominio.com']

3 - Instalar as libs:
    pip install gunicorn whitenoise
    whitenoise - para apresentar arquivos estáticos
    gunicorn - servidor para rodar a aplicação em produção

4 - No arquivo settings.py por 'whitenoise.middleware.WhiteNoiseMiddleware' aboixo de 'django.middleware.security.SecurityMiddleware',

5 - Conferir as variáveis estáticas no arquivo settings.py:
    STATIC_URL = 'static/' # Usado no desenvolvimento
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Usado na produção

6 - Criar o arquivo .gitignore para selecionar arquivos que não vão ser publicados
```
