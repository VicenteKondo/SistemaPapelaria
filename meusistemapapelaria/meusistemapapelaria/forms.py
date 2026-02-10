from django import forms
from .models import Itens, Colaborador, Cliente, ControleVendas
from django.forms import timezone

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'cargo']