# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Archive.full_path'
        db.delete_column(u'jaguar_archive', 'full_path')

        # Adding field 'Archive.filename'
        db.add_column(u'jaguar_archive', 'filename',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Archive.full_path'
        db.add_column(u'jaguar_archive', 'full_path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Archive.filename'
        db.delete_column(u'jaguar_archive', 'filename')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'b7610c65-7fba-4599-9239-f4e8ee257ba0'", 'max_length': '36'})
        }
    }

    complete_apps = ['jaguar']