from django.db import models

from candidatos.models import Eleicao

class Localidade(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE())
    sigla_localidade = models.CharField(max_length=2)
    nome_local = models.CharField(max_length=35)

    class Meta:
        verbose_name_plural = 'Localidades'