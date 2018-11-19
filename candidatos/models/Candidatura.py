from django.db import models


class Candidatura(models.Model):
    reeleicao = models.CharField(max_length=3)
    declaracao_bens = models.CharField(max_length=3)
    resultado_turno = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Candidatura'