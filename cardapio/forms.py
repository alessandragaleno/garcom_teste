# forms.py
from django import forms
from .models import Cardapio

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Cardapio
        fields = ['nome', 'preco', 'categoria']
