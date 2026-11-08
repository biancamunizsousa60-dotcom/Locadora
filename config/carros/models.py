from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    placa = models.CharField(max_length=8, unique=True)
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"