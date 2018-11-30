from django.db import models

from ..models import Eleicao

class Turno_Eleicao(models.Model):
    data_eleicao = models.DateField(help_text='Data da eleição')
    turno = models.IntegerField(help_text='1º ou 2º turno')
    eleicao = models.ForeignKey(Eleicao)

    class Meta:
        verbose_name_plural = 'Turnos da Eleição'

    def __str__(self):
        return "%dº turno (%s/%s/%s)" %(self.turno, str(self.data_eleicao.day), str(self.data_eleicao.month), str(self.data_eleicao.year))