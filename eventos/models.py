#-*- coding: utf-8 -*-

from django.db import models
#from django.db.models import signals

#from signals import create_slug

TIPO_EVENTO = (
    ('festa', 'Festa'),
    ('show', 'Show'),
)


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

    # Slug
    slug = models.SlugField(max_length=100, unique=True)
#    slug_field_name = 'slug'
#    slug_from = 'nome'

    def __unicode__(self):
        return self.nome

    class Meta():
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'


#signals.post_save.connect(create_slug, sender=Eventos)
