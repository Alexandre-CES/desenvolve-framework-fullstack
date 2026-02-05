from django.urls import path
from .views import lista_produto

urlpatterns = [
  path('produtos/', lista_produto, name='lista_produtos'),
]