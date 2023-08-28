from django.db import models

from garagem.models import Categoria, Cor, Acessorio, Modelo
from uploader.models import Image

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField( default = 0,null=True, blank=True, max_digits=10, decimal_places=2)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")

    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}, {self.cor}"
    
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
