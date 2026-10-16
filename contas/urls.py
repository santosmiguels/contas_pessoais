from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrarContas/', views.cadastrar_contas, name='cadastrar_contas'),
]