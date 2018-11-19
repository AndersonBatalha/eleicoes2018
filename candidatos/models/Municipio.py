from django.db import models


class Municipio(models.Model):
    nome_municipio = models.CharField(max_length=75)

    class Meta:
        verbose_name_plural = 'Municípios'