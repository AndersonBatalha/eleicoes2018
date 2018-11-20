from django.db import models

class Candidatura(models.Model):
    reeleicao = models.CharField(max_length=1)
    declaracao_bens = models.CharField(max_length=1)
    resultado_turno = models.CharField(max_length=50)

    def __str__(self):
        return self.resultado_turno