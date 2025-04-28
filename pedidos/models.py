from django.db import models
from produtos.models import Produtos

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Cliente'
    

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'pedidos'


class Pedidos_itens(models.Model):
    id_pedido_item = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)  # noqa: F821
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)  # noqa: F821

    class Meta:
        verbose_name_plural = 'Pedidos'
        