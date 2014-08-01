# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'LinkHistory', fields ['when']
        db.create_index(u'jaguar_linkhistory', ['when'])


    def backwards(self, orm):
        # Removing index on 'LinkHistory', fields ['when']
        db.delete_index(u'jaguar_linkhistory', ['when'])


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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c98d79d0-046d-4465-a5ff-5d3ace82d25d'", 'max_length': '36'})
        },
        u'jaguar.linkhistory': {
            'Meta': {'object_name': 'LinkHistory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Link']"}),
            'when': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['jaguar']