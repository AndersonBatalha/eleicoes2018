from django.shortcuts import render
from django.views.generic import View

from candidatos.models import Cargo, Candidato

'''
Descriçao: com base no cargo escolhido pelo usuario (governador ou presidente), o sistema ira retornar uma lista com os candidatos 
'''

class CandidatosCargo(View):
    context_dict = {}
    template = 'candidatos/candidatos_cargo.html'

    def get(self, request, c):
        try:
            cargo = Cargo.objects.get(desc_cargo__icontains=c)
            self.context_dict['cargo'] = cargo

            candidatos = Candidato.objects.filter(cargo = cargo)
        except Cargo.DoesNotExist:
            self.context_dict['candidatos'] = None

        print(self.context_dict)

        return render(request, self.template, context=self.context_dict)