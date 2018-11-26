from django.db import models

from .Estado_Nascimento import Estado_Nascimento

class Municipio(models.Model):
    nome_municipio = models.CharField(max_length=100, help_text="Município de nascimento do candidato", unique=True)
    UF = models.ForeignKey(Estado_Nascimento)

    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"

    def __str__(self):
        return "%s (%s)" %(self.nome_municipio, self.UF)