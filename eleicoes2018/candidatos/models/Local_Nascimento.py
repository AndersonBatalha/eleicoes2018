from django.db import models

from .Municipio import Municipio
from .Localidade import Localidade

class Local_Nascimento(models.Model):
    municipio = models.ForeignKey(Municipio)
    sigla_localidade = models.ForeignKey(Localidade)