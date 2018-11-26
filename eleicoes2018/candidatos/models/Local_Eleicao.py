from django.db import models

from .Eleicao import Eleicao

class Local_Eleicao(models.Model):
    abreviacao = models.CharField(max_length=3)
    nome_local = models.CharField(max_length=50, help_text="Local onde a eleição é disputada")
    eleicao = models.ForeignKey(Eleicao)

    class Meta:
        verbose_name_plural = "Locais de eleição"

    def __str__(self):
        return "%s (%s)" % (self.nome_local, self.abreviacao)
