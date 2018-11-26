from django.db import models


class Eleicao(models.Model):
    desc_eleicao = models.CharField(max_length=100, help_text="Descrição")
    ano_eleicao = models.IntegerField(help_text="Ano da eleição")
    abrangencia = models.CharField(max_length=30, help_text="Estadual ou Federal")

    class Meta:
        verbose_name = "Eleição"
        verbose_name_plural = "Eleições"

    def __str__(self):
        return self.desc_eleicao