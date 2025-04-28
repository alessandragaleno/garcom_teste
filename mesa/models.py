from django.db import models
from mesa.models import Mesa

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Mesa(models.Model):
    nome_mesa = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disponivel')
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    data_ocupacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_mesa} ({self.capacidade} pessoas) - {self.status}"

