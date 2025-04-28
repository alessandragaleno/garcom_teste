from django.db import models
from produtos.models import Produtos  # Importando o modelo de Produtos, do app produtos

# Modelo para a tabela Produtos
class Produtos(models.Model):  # noqa: F811
    # Criando uma chave estrangeira para relacionar com outro produto. 
    # Isso significa que o produto pode estar associado a outro produto (como um "produto relacionado", por exemplo).
    produto_id = models.ForeignKey('Produtos', on_delete=models.CASCADE)
    
    # Nome do produto, por exemplo: "Pizza Calabresa", "Refrigerante", etc.
    nome = models.CharField(max_length=100)
    
    # Preço do produto, usando DecimalField para garantir precisão em valores monetários.
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Categoria do produto. Esse campo representa a categoria (ex: "Pizza", "Bebidas").
    categoria = models.CharField(max_length=100)
    
    # Definindo como o Django vai se referir ao modelo no Admin
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

# Modelo para a tabela Categoria
class Categoria(models.Model):
    # Nome da categoria, por exemplo: "Pizza", "Bebidas", etc.
    nome = models.CharField(max_length=50)
    
    # Descrição mais detalhada sobre a categoria, explicando o que ela representa.
    descricao = models.TextField()

    # Definindo como o Django vai se referir ao modelo de Categoria no Admin
    class Meta:
        verbose_name = 'Categoria'

    # Método que define como a categoria será exibida. Quando você acessar o modelo, ele vai mostrar o nome.
    def __str__(self):
        return self.nome
