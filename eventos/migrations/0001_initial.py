# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Eventos'
        db.create_table('eventos_eventos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=54)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='Festa', max_length=10)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('sobre', self.gf('django.db.models.fields.TextField')()),
            ('atracoes', self.gf('django.db.models.fields.TextField')()),
            ('ingressos', self.gf('django.db.models.fields.TextField')()),
            ('informacoes', self.gf('django.db.models.fields.TextField')()),
            ('mapa', self.gf('django.db.models.fields.TextField')()),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('eventos', ['Eventos'])


    def backwards(self, orm):
        # Deleting model 'Eventos'
        db.delete_table('eventos_eventos')


    models = {
        'eventos.eventos': {
            'Meta': {'object_name': 'Eventos'},
            'atracoes': ('django.db.models.fields.TextField', [], {}),
            'data': ('django.db.models.fields.DateField', [], {}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'informacoes': ('django.db.models.fields.TextField', [], {}),
            'ingressos': ('django.db.models.fields.TextField', [], {}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'mapa': ('django.db.models.fields.TextField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '54'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'sobre': ('django.db.models.fields.TextField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'Festa'", 'max_length': '10'})
        }
    }

    complete_apps = ['eventos']