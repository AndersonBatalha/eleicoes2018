from django.contrib import admin

from .models import *

class CandidatoAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug_nome': ('nome_urna', ) }

admin.site.register(Candidatura)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Cargo)
admin.site.register(Coligacao)
admin.site.register(Coligacao_Partidos)
admin.site.register(Eleicao)
admin.site.register(Estado_Nascimento)
admin.site.register(Local_Eleicao)
admin.site.register(Municipio)
admin.site.register(Partido)
admin.site.register(Turno_Eleicao)