from django.shortcuts import render
from django.views.generic import View

from ..models import Cargo, Candidato, Local_Eleicao

'''
Descriçao: com base no cargo escolhido pelo usuario (governador ou presidente), o sistema ira retornar uma lista com os candidatos 
'''

class CandidatosCargo(View):
    context_dict = {}
    template = 'candidatos/candidatos_cargo.html'

    def get(self, request, cargo=None):
        try:
            self.cargo = Cargo.objects.get(desc_cargo__iexact=cargo)
            self.candidatos = Candidato.objects.filter(cargo = self.cargo).order_by('nome_urna')
            self.locais = Local_Eleicao.objects.all().exclude(abreviacao='BR')
        except Cargo.DoesNotExist:
            self.context_dict['cargo'] = None
            self.context_dict['candidatos'] = None

        self.context_dict['cargo'] = self.cargo
        self.context_dict['candidatos'] = self.candidatos
        self.context_dict['qtd_resultados'] = len(self.candidatos)
        self.context_dict['locais'] = self.locais

        return render(request, self.template, self.context_dict)