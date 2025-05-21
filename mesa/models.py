from django.db import models

class Mesa(models.Model):
    nome_mesa = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disponivel')
    data_ocupacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_mesa} {self.status}"


