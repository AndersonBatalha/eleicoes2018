from django.db import models

from .Eleicao import Eleicao

class Estado_Eleicao(models.Model):
    sigla = models.CharField(max_length=3)
    nome_estado = models.CharField(max_length=50, help_text="Estado onde a eleição é disputada")
    eleicao = models.ForeignKey(Eleicao)

    class Meta:
        verbose_name = "Eleição nos Estados"
        verbose_name_plural = "Estados"

    def __str__(self):
        return "%s (%s)" % (self.nome_estado, self.sigla)
