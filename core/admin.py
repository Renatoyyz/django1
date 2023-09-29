from django.contrib import admin

from .models import Cliente, Produtos

# As classes, com o atributo list_display, define como será mostrado o conteúdo no template admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email']

admin.site.register(Produtos, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
