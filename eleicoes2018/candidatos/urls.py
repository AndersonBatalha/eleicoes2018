"""eleicoes2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^$', Index.as_view(), name='index'),
    url(r'^candidatos/(?P<cargo>[\w\-]+)/$', CandidatosCargo.as_view(), name='candidatos_cargo'),
    url(r'^candidato/(?P<id>[\w\-]+)/$', DetalhesCandidato.as_view(), name='detalhes_candidato'),
    url(r'^candidatos/estado/(?P<uf>[\w\-]+)/$', CandidatosEstado.as_view(), name='candidatos_estado'),
]
