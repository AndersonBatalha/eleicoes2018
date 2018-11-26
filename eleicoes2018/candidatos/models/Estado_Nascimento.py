from django.db import models

from .Eleicao import Eleicao

class Estado_Nascimento(models.Model):
    UF = models.CharField(max_length=3, help_text="Unidade da Federação")

    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.UF
