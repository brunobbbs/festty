#-*- coding: utf-8 -*-

from festty.eventos.models import Eventos, Estado, Bairro
from django.contrib import admin

from festty.settings import STATIC_URL


class EventosAdmin(admin.ModelAdmin):

    class Media:
        js = ((STATIC_URL + 'js/tiny_mce/tiny_mce.js'), (STATIC_URL + 'js/tiny_mce/tiny_mce_config.js'), )

    list_display = ('nome', 'tipo', 'data', 'destaque')
    prepopulated_fields = {'slug': ('data', 'nome')}
    list_editable = ('destaque',)
    list_filter = ('destaque',)
    search_fields = ('nome',)
    exclude = ('destaque',)


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('uf',)
    search_fields = ('nome',)


admin.site.register(Eventos, EventosAdmin)
admin.site.register(Estado)
admin.site.register(Bairro, BairroAdmin)
