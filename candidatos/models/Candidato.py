from django.db import models

from candidatos.models import Candidatura, Cargo, Partido, Municipio

class Candidato(models.Model):
    candidatura = models.ForeignKey(Candidatura, on_delete=models.CASCADE())
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE())
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE())
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE())

    nome_completo = models.CharField(max_length=120)
    nome_urna = models.CharField(max_length=100)
    genero = models.CharField(max_length=25)
    grau_instrucao = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=35)
    raca = models.CharField(max_length=30)
    idade_data_posse = models.IntegerField()
    ocupacao = models.CharField(max_length=50)
    email_contato = models.EmailField()
    nacionalidade = models.CharField(max_length=25)
    data_nasc = models.DateField()
    numero_candidato = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Candidatos'