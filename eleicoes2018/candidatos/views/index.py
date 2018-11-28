from django.shortcuts import render
from django.views.generic import View

class Index(View):
    context_dict = {}
    msg = 'Index do site'
    template = 'candidatos/index.html'
    def get(self, request):
        self.context_dict['msg'] = self.msg
        return render(request, self.template, self.context_dict)