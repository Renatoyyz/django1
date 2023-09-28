from django.db import models

class Produtos(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preco", decimal_places=2, max_digits=8)
    estoque = models.IntegerField("Quantidade em estoque")

class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=50)
    sobrenome = models.CharField('SobreNome', max_length=50)
    email = models.EmailField('E-mail', max_length=50)