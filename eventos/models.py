#-*- coding: utf-8 -*-

from django.db import models

TIPO_EVENTO = (
    ('festa', 'Festa'),
    ('show', 'Show'),
)

UF = (
    ('DF', 'Distrito Federal'),
    ('GO', 'Goiás'),
)

class Estado(models.Model):
    sigla = models.CharField(max_length=2, choices=UF, unique=True)

    def __unicode__(self):
        return self.sigla

    class Meta():
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'


class Bairro(models.Model):
    uf = models.ForeignKey(Estado)
    nome = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nome

    class Meta():
        verbose_name = u'Bairro'
        verbose_name_plural = u'Bairros'



class Eventos(models.Model):

    # Dados do evento
    nome = models.CharField(max_length=54)
    tipo = models.CharField(choices=TIPO_EVENTO, default='Festa', max_length=10)
    data = models.DateField()
    hora = models.CharField(max_length=3)
    local = models.CharField(max_length=140)
    imagem = models.ImageField(upload_to='images/%Y/%m/%d')
    sobre = models.TextField()
    atracoes = models.TextField()
    ingressos = models.TextField()
    informacoes = models.TextField()
    mapa = models.TextField(blank=True)
    destaque = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)


    def __unicode__(self):
        return self.nome

    class Meta():
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'


