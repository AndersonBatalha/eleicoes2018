from django.db import models

class Candidatura(models.Model):
    reeleicao = models.CharField(max_length=1, help_text="Candidato disputa a reeleição? (S/N)")
    declaracao_bens = models.CharField(max_length=1, help_text="Candidato declarou bens? (S/N)")
    resultado_eleicao = models.CharField(max_length=50, help_text="Situação do candidato na eleição", default="nao eleito")

    class Meta:
        verbose_name_plural = "Candidaturas"

    def __str__(self):
        return self.resultado_eleicao