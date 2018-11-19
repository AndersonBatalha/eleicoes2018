from django.db import models


class Partido(models.Model):
    sigla_partido = models.CharField(max_length=3)
    nome_partido = models.CharField(max_length=50)
    numero_partido = models.IntegerField(default=0)

    class Meta:
        abstract = 'Partidos políticos no Brasil'
        verbose_name_plural = 'Partidos'