from django.db import models

from candidatos.models import Municipio, Localidade

class Local_Nascimento(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE())
    sigla_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE())