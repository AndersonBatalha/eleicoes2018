from django.db import models

from .Local_Eleicao import Local_Eleicao
from .Candidato import Candidato

class Coligacao(models.Model):
    nome_coligacao = models.CharField(max_length=200, help_text="Nome da coligação de partidos")
    local = models.ForeignKey(Local_Eleicao)
    candidatos = models.ManyToManyField(Candidato)

    class Meta:
        verbose_name = "Coligação"
        verbose_name_plural = "Coligações"

    def __str__(self):
        return "%s" %(self.nome_coligacao)

