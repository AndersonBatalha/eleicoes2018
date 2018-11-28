from django.db import models

from .Candidatura import Candidatura
from .Cargo import Cargo
from .Partido import Partido
from .Municipio import Municipio
from .Local_Eleicao import Local_Eleicao

class Candidato(models.Model):
    nome_completo = models.CharField(max_length=125, help_text="Nome completo")
    nome_urna = models.CharField(max_length=75, help_text="Nome na urna eletrônica")
    genero = models.CharField(max_length=35, help_text="Gênero")
    grau_instrucao = models.CharField(max_length=40, help_text="Escolaridade")
    estado_civil = models.CharField(max_length=40, help_text="Estado civil")
    idade_data_posse = models.IntegerField(help_text="Idade na data da posse")
    raca = models.CharField(max_length=50, help_text="Raça")
    ocupacao = models.CharField(max_length=80, help_text="Ocupação")
    email_contato = models.EmailField(help_text="E-mail")
    nacionalidade = models.CharField(max_length=50, help_text="Nacionalidade")
    data_nasc = models.DateField(help_text="Data de nascimento")
    numero_candidato = models.IntegerField(help_text="Número do candidato")

    cargo = models.ForeignKey(Cargo)
    partido = models.ForeignKey(Partido)
    municipio = models.ForeignKey(Municipio)
    candidatura = models.ForeignKey(Candidatura)
    local_eleicao = models.ForeignKey(Local_Eleicao)

    class Meta:
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.nome_urna