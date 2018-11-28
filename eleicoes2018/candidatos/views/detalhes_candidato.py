from django.shortcuts import render
from django.views.generic import View

from ..models import *


class DetalhesCandidato(View):
    context_dict = {}
    template = 'candidatos/detalhes.html'

    def get(self, request, id=None):
        try:
            candidato = Candidato.objects.get(pk=id)
            cargo = Cargo.objects.get(desc_cargo=candidato.cargo.desc_cargo)
            partido = Partido.objects.get(sigla_partido=candidato.partido.sigla_partido)
            municipio = Municipio.objects.get(nome_municipio=candidato.municipio.nome_municipio)
            candidatura = Candidatura.objects.get(pk=candidato.candidatura_id)
            local_eleicao = Local_Eleicao.objects.get(abreviacao=candidato.local_eleicao.abreviacao)

        except Candidato.DoesNotExist or Candidato.MultipleObjectsReturned:
            candidato = None
            cargo = None
            partido = None
            municipio = None
            candidatura = None
            local_eleicao = None

        self.context_dict['candidato'] = candidato
        self.context_dict['cargo'] = cargo
        self.context_dict['partido'] = partido
        self.context_dict['municipio'] = municipio
        self.context_dict['candidatura'] = candidatura
        self.context_dict['local'] = local_eleicao

        return render(request, self.template, self.context_dict)
