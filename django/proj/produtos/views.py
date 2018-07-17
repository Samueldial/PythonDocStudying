from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    nome = 'Django'
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def produto(request, codigo):
    produto = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto': produto})
