from django.shortcuts import render
from django.views.generic import View

from ..models import *


class DetalhesCandidato(View):
    context_dict = {}
    template = 'candidatos/detalhes.html'
    candidato = None
    cargo = None
    partido = None
    municipio = None
    candidatura = None
    local_eleicao = None
    partidos_coligacao = None

    def get(self, request, id=None):
        try:
            self.candidato = Candidato.objects.get(pk=id)
            self.local_eleicao = Local_Eleicao.objects.get(abreviacao=self.candidato.local_eleicao.abreviacao)
            self.coligacao = Coligacao.objects.get(local=self.local_eleicao, candidatos=self.candidato)
            self.partido = Partido.objects.get(sigla_partido=self.candidato.partido.sigla_partido)
            self.partidos_coligacao = Coligacao_Partidos.objects.filter(coligacao=self.coligacao, partido=self.partido)
            self.cargo = Cargo.objects.get(desc_cargo=self.candidato.cargo.desc_cargo)
            self.municipio = Municipio.objects.get(nome_municipio=self.candidato.municipio.nome_municipio)
            self.candidatura = Candidatura.objects.get(pk=self.candidato.candidatura_id)

        except Candidato.DoesNotExist:
            self.candidato = None
        except Coligacao.DoesNotExist:
            self.coligacao = None

        print (self.local_eleicao)
        self.context_dict['candidato'] = self.candidato
        self.context_dict['cargo'] = self.cargo
        self.context_dict['partido'] = self.partido
        self.context_dict['municipio'] = self.municipio
        self.context_dict['candidatura'] = self.candidatura
        self.context_dict['local'] = self.local_eleicao
        self.context_dict['coligacao'] = self.coligacao
        if self.partidos_coligacao != None:
            self.context_dict['partidos'] = self.partidos_coligacao[0].partido.all()

        return render(request, self.template, self.context_dict)
