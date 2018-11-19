from django.db import models

from candidatos.models import Partido


class Coligacao(models.Model):
    sigla_partido = models.ForeignKey(Partido, on_delete=models.CASCADE())
    nome_coligacao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Coligações'