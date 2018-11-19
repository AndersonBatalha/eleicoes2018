from django.db import models


class Cargo(models.Model):
    desc_cargo = models.CharField(max_length=20)

    class Meta:
        abstract = 'Cargo pretendido pelo candidato'
        verbose_name_plural = 'Cargos'