from django import forms
from .models import Itens, Colaborador, Cliente, ControleVendas
from django.forms import timezone

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'cargo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome_completo', 'email', 'telefone', 'endereco', 'cpf']

class ItensForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ['nome_item', 'descricao', 'data_aquisicao', 'min_estoque', 'max_estoque', 'valor_venda', 'valor_custo', 'estoque_atual']        