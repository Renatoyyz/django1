from django.db import models

class Produtos(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preco", decimal_places=2, max_digits=8)
    estoque = models.IntegerField("Quantidade em estoque")

    # O método string serve para retornar um nome desejado para o objeto criado
    def __str__(self) -> str:
        return f'Produto: {self.nome} - Preço: R${self.preco}'

class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=50)
    sobrenome = models.CharField('SobreNome', max_length=50)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'