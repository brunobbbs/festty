#-*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

import calendar
from datetime import date


MESES = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril',
         '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto', '09':'Setembro',
         '10':'Outubro', '11':'Novembro', '12':'Dezembro'}

MONTHNAME = {'January':'Janeiro', 'February':'Fevereiro', 'March':'Março', 'April':'Abril',
             'May':'Maio', 'June':'Junho', 'July':'Julho', 'August':'Agosto', 'September':'Setembro',
             'October':'Outubro', 'November':'Novembro', 'December':'Dezembro', 'Jan':'Jan', 'Feb':'Fev',
             'Mar':'Mar', 'Apr':'Abr', 'May':'Mai', 'Jun':'Jun', 'Jul':'Jul', 'Aug':'Ago', 'Sep':'Set', 
             'Oct':'Out', 'Nov':'Nov', 'Dec':'Dez'}

def get_date():

    dia = "%02d" % date.today().day
    mes = "%02d" % date.today().month
    ano = date.today().year

    return [ano, mes, dia]


ANO_ATUAL = get_date()[0]
MES_ATUAL = get_date()[1]
DIA_ATUAL = get_date()[2]

mes_selecionado = MESES[MES_ATUAL]


# Gera os dias do mês para barra de calendário
def dias(request):
    
    get_mes = request.GET.get('mes', MES_ATUAL)
    mes = int(get_mes)

    dias_mes = calendar.monthcalendar(ANO_ATUAL, mes)

    dia = []
    for dias in dias_mes:
        for l in dias:
            if l != 0:
                parseDia = date(ANO_ATUAL, mes, l)
                sDia = parseDia.weekday()

                if sDia == 4:
                    diaSemana = 'sexta'

                elif sDia == 5:
                    diaSemana = 'sabado'

                elif sDia == 6:
                    diaSemana = 'domingo'

                else:
                    diaSemana = 'normal'

                dia.append({'dia':'%02d' % l, 'mes':'%02d' % mes, 'dia_semana':diaSemana, 'ano':ANO_ATUAL})


    context = RequestContext(request)

    return render_to_response('dias.html', dict(dias=dia), context)


def calendario(request):
    return render_to_response('calendario.html', {'mes_selecionado':mes_selecionado}, RequestContext(request))
