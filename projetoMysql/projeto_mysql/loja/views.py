from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm, ProdutoModelForm

# Create your views here.
def lista_produtos(request):
  produtos = Produto.objects.all()
  return render(request, 'produtos.html', {'produtos':produtos})

def cadastrar_produto(request):
  if request.method == 'POST':
    form = ProdutoModelForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_produtos')
  else:
    form = ProdutoModelForm()
  
  return render(request, 'cadastrar_produto.html', {'form':form})