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