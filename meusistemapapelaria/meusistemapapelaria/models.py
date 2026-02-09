from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=225)
    cargo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome_completo
    
class Itens(models.Model):
    nome_item = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição", blank=True, null=True)
    min_estoque = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estoque Mínimo", blank=True,null=True)
    max_estoque = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estoque Máximo", blank=True,null=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Venda", blank=True,null=True)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Custo", blank=True,null=True)
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estoque Atual", blank=True,null=True)
    
    def __str__(self):
        return self.nome_item
    
class Cliente(models.Model):
    nome_completo = models.CharField(max_length=225)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)

class ControleVendas(models.Model):
    STATUS_CHOICES = [
        ('Vendido', 'Vendido'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado'),

    ]

    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        verbose_name="Cliente"
    )

    item = models.ForeignKey(
        'Itens',
        on_delete=models.CASCADE,
        verbose_name="Itens"
    )

    data_venda = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f"{self.item.nome_item} para {self.cliente.nome_completo}"
