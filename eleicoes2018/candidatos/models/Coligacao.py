from django.db import models

from .Partido import Partido

class Coligacao(models.Model):
    sigla_partido = models.ManyToManyField(Partido)
    nome_coligacao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_coligacao

