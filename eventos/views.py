#-*- coding: utf-8 -*_

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from models import Eventos
from django.contrib.sites.models import Site

# Importando dados de data da app calendario
from festty.calendario.views import ANO_ATUAL, MES_ATUAL, DIA_ATUAL, MESES


def index(request):
    """
    Home page
    """
    eventos = Eventos.objects.filter(destaque=True).order_by('data')[:4]

    return render_to_response('index.html', dict(eventos=eventos, mes=MESES[MES_ATUAL]),RequestContext(request))


def listar(request, ano=ANO_ATUAL, mes=MES_ATUAL, dia=DIA_ATUAL):
    """
    Listar todos os eventos
    """
    # Obter eventos da data selecionada
    eventos = Eventos.objects.filter(data__year=ano).\
                                filter(data__month=mes).\
                                filter(data__day=dia)

    # absolute url
    absolute_url = 'http://%s' % Site.objects.get_current().domain
    return render_to_response('listar.html', dict(eventos=eventos, absolute_url=absolute_url, mes=MESES[mes], dia=dia), RequestContext(request))


def informacoes(request, slug=None):
    """
    Exibir informações de um evento específico
    """
    evento = get_object_or_404(Eventos, slug=slug)
    return render_to_response('informacoes.html', dict(evento=evento, mes=MESES[evento.data.strftime('%m')]), RequestContext(request))


def chamada(request):
    """
    """
    return render_to_response('anuncie_chamada.html', dict(mes=MESES[MES_ATUAL]),RequestContext(request))


def destaque(request):
    """
    """
    return render_to_response('anuncie_destaque.html', dict(mes=MESES[MES_ATUAL]),RequestContext(request))


def publique(request):
    """
    """
    return render_to_response('publique.html', dict(mes=MESES[MES_ATUAL]),RequestContext(request))

