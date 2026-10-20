from django.shortcuts import render, redirect
from .models import ContasPessoais

# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastrar_contas(request):
    if request.method == 'POST':
        nome_conta = request.POST.get('nome_conta')
        fornecedor = request.POST.get('fornecedor')

        ContasPessoais.objects.create(
            nome_conta = nome_conta,
            fornecedor = fornecedor,
        )
    return render(request, "cadastrar_contas.html")

def atualizar_contas(request):
    query = request.GET.get('get', '')
    contaspessoais = ContasPessoais.objects.filter(nome_conta__icontains=query)
    return render(request, 'atualizar_contas.html', {
        'contaspessoais': contaspessoais,
        'query': query,
    })
    #return render(request, 'atualizar_contas.html')



def pesquisar_contas(request):
    query = request.GET.get('get', '')
    contaspessoais = ContasPessoais.objects.filter(nome_conta__icontains=query)
    return render(request, 'pesquisar_contas.html', {
        'contaspessoais': contaspessoais,
        'query': query,
    })


def remover_contas(request):
    query = request.GET.get('get', '')
    contaspessoais = ContasPessoais.objects.filter(nome_conta__icontains=query)
    return render(request, 'pesquisar_contas.html', {
        'contaspessoais': contaspessoais,
        'query': query,
    })
#    contas = ContasPessoais.objects.get(código_contas=código_contas)
#    contas.delete()
#    return redirect('index')
"""
    query = request.GET.get('get', '')
    contaspessoais = ContasPessoais.objects.filter(nome_conta__icontains=query)
    return render(request, 'remover_contas.html', {
        'contaspessoais': contaspessoais,
        'query': query,
    })
"""