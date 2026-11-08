from django.core.exceptions import ValidationError
from django.db import models
from carros.models import Carro
from clientes.models import Cliente

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0,
    editable=False)
    ativa = models.BooleanField(default=True)

    def clean(self):
            if self.data_devolucao < self.data_retirada:
                raise ValidationError('A devolução não pode ser antes da retirada.')

    def save(self, *args, **kwargs):
            dias = max((self.data_devolucao - self.data_retirada).days, 1)
            self.valor_total = dias * self.carro.valor_diaria
            super().save(*args, **kwargs)
            self.carro.disponivel = not self.ativa
            self.carro.save()

    def __str__(self):
        return f"{self.cliente} - {self.carro}"