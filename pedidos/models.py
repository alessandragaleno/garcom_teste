from django.db import models
from produtos.models import Produtos    # Certifique-se que este caminho está correto

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_pedido = models.DateField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f'Pedido #{self.id_pedido} - Cliente {self.id_cliente}'


class PedidoItem(models.Model):
    id_pedido_item = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pedidos_itens'
        verbose_name = 'Item de Pedido'
        verbose_name_plural = 'Itens de Pedido'


    def __str__(self):
        return f'Item #{self.id_pedido_item} do Pedido #{self.id_pedido.id_pedido}'
