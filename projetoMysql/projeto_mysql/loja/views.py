from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm, ProdutoModelForm
from django.core.mail import send_mail
from .forms import ContatoForm

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

def contato(request):
  enviado = False
  if request.method == 'POST':
    form = ContatoForm(request.POST)
    if form.is_valid():
      nome = form.cleaned_data['nome']
      email = form.cleaned_data['email']
      mensagem = form.cleaned_data['mensagem']
      assunto = f'Contato de {nome}'
      mensagem_completa = f'Nome: {nome}\nE-mail {email}\nMensagem\n{mensagem}'

      send_mail(
        assunto,
        mensagem_completa,
        'seuemail@gmail.com',
        'destinatario@gmail.com',
        fail_silently = False,
      )
      enviado = True
  else:
    form = ContatoForm()

  return render(request, 'contato.html', {'form':form, 'enviado':enviado})