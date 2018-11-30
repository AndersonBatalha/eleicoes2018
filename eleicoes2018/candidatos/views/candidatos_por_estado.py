from django.shortcuts import render
from django.views.generic import View

from ..models import Local_Eleicao, Candidato, Cargo

class CandidatosEstado(View):
    context_dict = {}
    template = 'candidatos/candidatos_estado.html'
    def get(self, request, uf=None):
        try:
            localidade = Local_Eleicao.objects.get(abreviacao__iexact=uf)
            self.locais = Local_Eleicao.objects.all().exclude(abreviacao='BR')
            cargo = Cargo.objects.get(desc_cargo__iexact='governador')
            candidatos = Candidato.objects.filter(local_eleicao=localidade, cargo = cargo).order_by('nome_urna')
            self.context_dict['qtd_resultados'] = len(candidatos)
        except Local_Eleicao.DoesNotExist:
            localidade, cargo, candidatos = None, None, None

        self.context_dict['local'] = localidade
        self.context_dict['cargo'] = cargo
        self.context_dict['candidatos'] = candidatos
        self.context_dict['locais'] = self.locais

        return render(request, self.template, self.context_dict)


