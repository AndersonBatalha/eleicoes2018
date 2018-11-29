from django.shortcuts import render
from django.views.generic import View

from ..models import Partido

'''
Descriçao: com base no cargo escolhido pelo usuario (governador ou presidente), o sistema ira retornar uma lista com os candidatos 
'''

class ListarPartidos(View):
    context_dict = {}
    template = 'candidatos/partidos.html'

    def get(self, request, cargo=None):
        self.partidos = Partido.objects.all()
        self.context_dict['partidos'] = self.partidos
        self.context_dict['qtd_resultados'] = len(self.partidos)


        print(self.context_dict)

        return render(request, self.template, self.context_dict)