from django.contrib import admin
from .models import *


class ItemCarrinhoInline(admin.TabularInline):
    model = Carrinho.itens.through
    extra = 3


class VendaProdutoInline(admin.TabularInline):
    model = Venda.produtos.through
    extra = 3


class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 3


class CarrinhoAdmin(admin.ModelAdmin):
    inlines = (ItemCarrinhoInline,)


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor_total', )
    inlines = (
        VendaProdutoInline,
    )


class ProdutoAdmin(admin.ModelAdmin):
    inlines = (
        ImagemProdutoInline,
    )


# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemVenda)
admin.site.register(Endereco)
admin.site.register(Categoria)
admin.site.register(AvaliacaoProduto)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Oferta)
