from django.db import models

from .Coligacao import Coligacao
from .Partido import Partido

class Coligacao_Partidos(models.Model):
    coligacao = models.ForeignKey(Coligacao)
    partido = models.ManyToManyField(Partido)

    class Meta:
        verbose_name_plural = "Coligações e Partidos"

    def __str__(self):
        return self.coligacao, self.partido