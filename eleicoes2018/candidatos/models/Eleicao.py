from django.db import models


class Eleicao(models.Model):
    turno = models.IntegerField()
    desc_eleicao = models.CharField(max_length=50)
    data_eleicao = models.DateField()
    ano_eleicao = models.IntegerField()
    abrangencia = models.CharField(max_length=30)

    def __str__(self):
        return self.desc_eleicao