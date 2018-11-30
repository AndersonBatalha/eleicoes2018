from django.shortcuts import render
from django.views.generic import View


class Index(View):
    context_dict = {}
    template = 'candidatos/index.html'

    def get(self, request):
        texto1 = ['''O Poder Executivo tem a função de governar o povo e administrar os interesses públicos, de acordo com as leis previstas na Constituição Federal. No Brasil, País que adota o regime presidencialista, o líder do Poder Executivo é o Presidente da República, que tem o papel de chefe de Estado e de governo. O Presidente é eleito democraticamente para mandato com duração de quatro anos e possibilidade de uma reeleição consecutiva para igual período.''', '''Ao tomar posse, o chefe do Executivo tem o dever de sustentar a integridade e a independência do Brasil, apresentar um plano de governo com programas prioritários, projeto de lei de diretrizes orçamentárias e as propostas de orçamento. Cabe ao Poder Executivo executar as leis elaboradas pelo Poder Legislativo, mas o Presidente da República também pode iniciar esse processo. Em caso de relevância e urgência, adota medidas provisórias e propõe emendas à Constituição, projetos de leis complementares e ordinárias e leis delegadas.''', '''O Presidente da República também tem o direito de rejeitar ou sancionar matérias e ainda, decretar intervenção federal nos Estados, o estado de defesa e o estado de sítio; manter relações com Estados estrangeiros e credenciar seus representantes diplomáticos; celebrar tratados, convenções e atos internacionais, sujeitos a referendo do Congresso Nacional. Compete ao cargo a concessão de indulto e a comutação de penas, ou seja, substituir uma pena mais grave, imposta ao réu, por outra mais branda.''']

        texto2 = ['''Cabe ao governador exercer a direção superior da administração estadual e nomear secretários e altos dirigentes das empresas estatais. Além disso, propõe, aprova ou veta leis, e baixa decretos e regulamentos.''',
        '''Sobre a questão financeira, o governador negocia com ministros e com o presidente da República o recebimento de verbas para o Estado que ele representa. Apresenta à Assembleia Legislativa documentos com os planos orçamentários dos próximos anos.''',
        '''Outra função do governador é implementar políticas públicas e programas estaduais em áreas como saúde e educação. Para isso, conta com o auxílio dos secretários estaduais.''']

        urls = ['http://www2.planalto.gov.br/conheca-a-presidencia/presidencia/presidenta/atribuicoes',
                'https://g1.globo.com/politica/eleicoes/2018/noticia/2018/09/14/funciona-assim-o-que-faz-o-governador.ghtml']

        self.context_dict['texto1'] = texto1
        self.context_dict['texto2'] = texto2
        self.context_dict['urls'] = urls

        return render(request, self.template, self.context_dict)