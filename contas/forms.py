
from django import forms
from .models import ContasPessoais

class ContasPessoaisForm(forms.ModelForm):
     class Meta:
          model = ContasPessoais
          fields = ['nome_conta', 'fornecedor']
          widgets = {
                'nome_conta': forms.TextInput(
                    attrs={                         
                         'class':"form_control",
                         'id':"nome_conta",
                         'required':True,
                    },
               ),
               'fornecedor':forms.TextInput(
                    attrs={
                         'class':"forms.-control",
                         'id':"nome_conta",
                         'required':True                         
                    },                    
               ),
          }