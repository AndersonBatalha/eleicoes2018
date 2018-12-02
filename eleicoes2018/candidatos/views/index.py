from django.shortcuts import render
from django.views.generic import View

class Index(View):
    context_dict = {}
    template = 'candidatos/index.html'

    def get(self, request):

        urls = ['http://www2.planalto.gov.br/conheca-a-presidencia/presidencia/presidenta/atribuicoes',
                'https://g1.globo.com/politica/eleicoes/2018/noticia/2018/09/14/funciona-assim-o-que-faz-o-governador.ghtml']

        self.context_dict['urls'] = urls

        return render(request, self.template, self.context_dict)