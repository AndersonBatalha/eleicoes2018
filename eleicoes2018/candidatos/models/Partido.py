from django.db import models

class Partido(models.Model):
    sigla_partido = models.CharField(max_length=10, help_text="Sigla do partido", unique=True)
    nome_partido = models.CharField(max_length=50, help_text="Nome do partido")
    numero_partido = models.IntegerField(help_text="Número do partido na urna")

    class Meta:
        verbose_name_plural = "Partidos"

    def __str__(self):
        return "%s (%s)" %(self.nome_partido, self.sigla_partido)