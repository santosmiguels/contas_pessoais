from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrarContas/', views.cadastrar_contas, name='cadastrar_contas'),
    path('atualizarContas/', views.atualizar_contas, name='atualizar_contas'),
    path('pesquisarContas/', views.pesquisar_contas, name='pesquisar_contas'),
    path('removerContas/', views.remover_contas, name='remover_contas'),
]