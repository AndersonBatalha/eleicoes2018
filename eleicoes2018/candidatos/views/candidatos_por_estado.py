from django.shortcuts import render
from django.views.generic import View

from ..models import Local_Eleicao, Candidato, Cargo

class CandidatosEstado(View):
    context_dict = {}
    template = 'candidatos/candidatos_estado.html'
    locais_eleicao = None
    localidade = None
    cargo = None
    candidatos = None

    def get(self, request, uf=None):
        try:
            self.localidade = Local_Eleicao.objects.get(abreviacao__iexact=uf)
            self.locais = Local_Eleicao.objects.all().exclude(abreviacao='BR')
            self.cargo = Cargo.objects.get(desc_cargo__iexact='governador')
            self.candidatos = Candidato.objects.filter(local_eleicao=self.localidade, cargo = self.cargo).order_by('nome_urna')
            self.context_dict['qtd_resultados'] = len(self.candidatos)
        except Local_Eleicao.DoesNotExist:
            self.localidade, self.locais, self.cargo, self.candidatos = None, None, None, None

        self.context_dict['local'] = self.localidade
        self.context_dict['cargo'] = self.cargo
        self.context_dict['candidatos'] = self.candidatos
        self.context_dict['locais'] = self.locais

        return render(request, self.template, self.context_dict)


