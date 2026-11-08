from django import forms
from .models import Locacao

class LocacaoForm(forms.ModelForm):
class Meta:
    model = Locacao
    fields = ['cliente', 'carro', 'data_retirada', 'data_devolucao']
    widgets = {
    'data_retirada': forms.DateInput(attrs={'type': 'date'}),
    'data_devolucao': forms.DateInput(attrs={'type': 'date'}),
    }