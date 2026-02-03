from django.contrib import admin
from .models import Produto, Categoria

class ProdutpAdmin(admin.ModelAdmin):
  list_display = ('nome', 'preco', 'descricao')
  search_fields = ('nome', 'descricao')
  list_filter = ('preco',)
  list_editable = ('preco',)

admin.site.register(Produto, ProdutpAdmin)
admin.site.register(Categoria)