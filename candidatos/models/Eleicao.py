from django.db import models


class Eleicao(models.Model):
    turno = models.IntegerField()
    desc_eleicao = models.TextField()
    data_eleicao = models.DateField()
    ano_eleicao = models.IntegerField()
    abrangencia = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Eleições'