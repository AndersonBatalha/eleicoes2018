from django.db import models

from .Candidatura import Candidatura
from .Cargo import Cargo
from .Partido import Partido
from .Municipio import Municipio

class Candidato(models.Model):
    nome_completo = models.CharField(max_length=125)
    nome_urna = models.CharField(max_length=75)
    genero = models.CharField(max_length=35)
    grau_instrucao = models.CharField(max_length=40)
    estado_civil = models.CharField(max_length=40)
    idade_data_posse = models.IntegerField()
    raca = models.CharField(max_length=50)
    ocupacao = models.CharField(max_length=80)
    email_contato = models.EmailField()
    nacionalidade = models.CharField(max_length=50)
    data_nasc = models.DateField()
    numero_candidato = models.IntegerField()

    cargo = models.ForeignKey(Cargo)
    partido = models.ForeignKey(Partido)
    municipio = models.ForeignKey(Municipio)
    candidatura = models.ForeignKey(Candidatura)

    def __str__(self):
        return self.nome_urna