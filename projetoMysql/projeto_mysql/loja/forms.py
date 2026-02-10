from django import forms
from .models import Produto

class ProdutoForm(forms.Form):
  nome = forms.CharField(max_length=100, label='Nome do Produto')
  preco = forms.DecimalField(max_digits=10, decimal_places=2, label='Preço')
  descricao = forms.CharField(widget=forms.Textarea, label='Descrição')

class ProdutoModelForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = ['nome', 'preco', 'descricao']