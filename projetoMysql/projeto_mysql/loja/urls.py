from django.urls import path
from .views import (
  lista_produtos, 
  cadastrar_produto, 
  contato, 
  salvar_nome_na_sessao, 
  mostrar_nome_da_sessao, 
  limpar_sessao, 
  home
)

urlpatterns = [
  path('home/', home, name='home'),
  path('produtos/', lista_produtos, name='lista_produtos'),
  path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
  path('contato/', contato, name='contato'),
  path('salvar/', salvar_nome_na_sessao, name='salvar_nome'),
  path('mostrar/', mostrar_nome_da_sessao, name='mostrar_nome'),
  path('limpar/', limpar_sessao, name='limpar_sessao'),
]