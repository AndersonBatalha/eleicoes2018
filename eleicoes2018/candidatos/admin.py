from django.contrib import admin

from .models import *

admin.site.register(Candidatura)
admin.site.register(Candidato)
admin.site.register(Cargo)
admin.site.register(Coligacao)
admin.site.register(Coligacao_Partidos)
admin.site.register(Eleicao)
admin.site.register(Estado_Nascimento)
admin.site.register(Local_Eleicao)
admin.site.register(Municipio)
admin.site.register(Partido)
admin.site.register(Turno_Eleicao)