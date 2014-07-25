# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Archive.status'
        db.add_column(u'jaguar_archive', 'status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Archive.status'
        db.delete_column(u'jaguar_archive', 'status')


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
            'expiryDate': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b14bf3e7-a4db-4030-b553-7446478a0f0e'", 'max_length': '36'})
        }
    }

    complete_apps = ['jaguar']