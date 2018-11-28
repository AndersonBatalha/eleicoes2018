from django.shortcuts import render
from django.views.generic import View

from ..models import Cargo, Candidato

'''
Descriçao: com base no cargo escolhido pelo usuario (governador ou presidente), o sistema ira retornar uma lista com os candidatos 
'''

class CandidatosCargo(View):
    context_dict = {}
    template = 'candidatos/candidatos_cargo.html'

    def get(self, request, cargo=None):
        try:
            self.cargo = Cargo.objects.filter(desc_cargo__icontains=cargo)
            print(self.cargo)
            self.candidatos = Candidato.objects.filter(cargo = self.cargo).order_by('partido', 'cargo')
        except Cargo.DoesNotExist:
            self.context_dict['cargo'] = None
            self.context_dict['candidatos'] = None

        self.context_dict['cargo'] = self.cargo
        self.context_dict['candidatos'] = self.candidatos
        self.context_dict['qtd_resultados'] = len(self.candidatos)


        print(self.context_dict)

        return render(request, self.template, self.context_dict)