from django.shortcuts import render
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


"""
def novo_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf =  request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')

        Paciente.objects.create(
            nome = nome,
            cpf = cpf,
            email = email,
            telefone = telefone,
            data_nascimento = data_nascimento,
        )
        return redirect('novo_paciente_sucesso')
    return render(request, "novo-paciente.html")


class ContasPessoais(models.Model):
    código_contas = models.AutoField(primary_key=True)
    nome_conta = models.CharField(null=False, blank=False)
    fornecedor = models.CharField(null=False, blank=False)

    def __str__(self):
        return self.nome_conta



    
"""