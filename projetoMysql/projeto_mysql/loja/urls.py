from django.urls import path
from .views import lista_produtos, cadastrar_produto

urlpatterns = [
  path('produtos/', lista_produtos, name='lista_produtos'),
  path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
]