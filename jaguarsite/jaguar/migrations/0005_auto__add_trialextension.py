# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrialExtension'
        db.create_table(u'jaguar_trialextension', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=12, primary_key=True)),
            ('trialkey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.TrialKey'])),
            ('applied', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('organization_user', self.gf('django.db.models.fields.CharField')(default='', max_length=12)),
            ('history', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'jaguar', ['TrialExtension'])


    def backwards(self, orm):
        # Deleting model 'TrialExtension'
        db.delete_table(u'jaguar_trialextension')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '2000'}),
            'show_in_downloads': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'6e8faac8-ec0c-4b34-b200-93cde8e62d1a'", 'max_length': '36', 'db_index': 'True'})
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
        },
        u'jaguar.trialextension': {
            'Meta': {'object_name': 'TrialExtension'},
            'applied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '12', 'primary_key': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'organization_user': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12'}),
            'trialkey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.TrialKey']"})
        },
        u'jaguar.trialkey': {
            'Meta': {'object_name': 'TrialKey'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'v2c': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['jaguar']