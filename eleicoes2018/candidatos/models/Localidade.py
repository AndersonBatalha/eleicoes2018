from django.db import models

from .Eleicao import Eleicao

class Localidade(models.Model):
    eleicao = models.ForeignKey(Eleicao)
    sigla_localidade = models.CharField(max_length=2)
    local = models.CharField(max_length=75)

