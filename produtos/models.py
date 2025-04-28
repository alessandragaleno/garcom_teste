from django.db import models
from mesa.models import Mesa

# Modelo para as Categorias de Produtos
class Categorias(models.Model):
    # O nome da categoria, por exemplo: "Pizza", "Bebidas", etc.
    nome = models.CharField(max_length=255)
    
    # Descrição da categoria. Pode ser uma explicação mais detalhada sobre a categoria.
    descricao = models.TextField()

    # Método que define como o nome da categoria será exibido
    def __str__(self):
        return self.nome

# Modelo para os Produtos
class Produto(models.Model):  # noqa: F811
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do produto'
    )
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='Categoria de produto',
    )
    estoque = models.FloatField(
        verbose_name='Estoque produtos',
    )

    # Configuração para nomear o modelo no Django Admin
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    # Método que define como o produto será exibido quando for chamado, por exemplo, no Django Admin.
    def __str__(self):
        return self.nome
