from django.shortcuts import render
from django.views.generic import View

from ..models import Local_Eleicao, Candidato

class CandidatosEstado(View):
    context_dict = {}
    template = 'candidatos/candidatos_estado.html'
    def get(self, request, uf=None):
        try:
            localidade = Local_Eleicao.objects.get(abreviacao__iexact=uf)
            candidatos = Candidato.objects.filter(local_eleicao=localidade)
            self.context_dict['qtd_resultados'] = len(candidatos)
        except Local_Eleicao.DoesNotExist:
            localidade, candidatos = None, None

        self.context_dict['local'] = localidade
        self.context_dict['candidatos'] = candidatos

        return render(request, self.template, self.context_dict)


