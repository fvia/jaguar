# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LinkHistory.country'
        db.add_column(u'jaguar_linkhistory', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'LinkHistory.city'
        db.add_column(u'jaguar_linkhistory', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'LinkHistory.dns'
        db.add_column(u'jaguar_linkhistory', 'dns',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LinkHistory.country'
        db.delete_column(u'jaguar_linkhistory', 'country')

        # Deleting field 'LinkHistory.city'
        db.delete_column(u'jaguar_linkhistory', 'city')

        # Deleting field 'LinkHistory.dns'
        db.delete_column(u'jaguar_linkhistory', 'dns')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        u'jaguar.customer': {
            'Meta': {'object_name': 'Customer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'jaguar.link': {
            'Meta': {'object_name': 'Link'},
            'archive': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Archive']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Customer']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NEW'", 'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'afeb3f47-afbb-4073-be55-fdeddde5e048'", 'max_length': '36', 'db_index': 'True'})
        },
        u'jaguar.linkhistory': {
            'Meta': {'object_name': 'LinkHistory'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'dns': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Link']"}),
            'when': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['jaguar']