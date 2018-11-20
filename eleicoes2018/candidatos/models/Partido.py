from django.db import models


class Partido(models.Model):
    sigla_partido = models.CharField(max_length=2)
    nome_partido = models.CharField(max_length=50)
    numero_partido = models.IntegerField()

    def __str__(self):
        return "%s (%s)" %(self.nome_partido, self.sigla_partido)