# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'LicenseKeyUpdate.modified'
        db.delete_column(u'jaguar_licensekeyupdate', 'modified')

        # Adding field 'LicenseKey.modified'
        db.add_column(u'jaguar_licensekey', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 9, 27, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'LicenseKeyUpdate.modified'
        db.add_column(u'jaguar_licensekeyupdate', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 9, 27, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'LicenseKey.modified'
        db.delete_column(u'jaguar_licensekey', 'modified')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '2000'}),
            'show_in_downloads': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        u'jaguar.customer': {
            'Meta': {'object_name': 'Customer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'jaguar.licensekey': {
            'Meta': {'object_name': 'LicenseKey'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Customer']"}),
            'history': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'key_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 9, 27, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        u'jaguar.licensekeyupdate': {
            'Meta': {'object_name': 'LicenseKeyUpdate'},
            'applied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.LicenseKey']"}),
            'time_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'v2c': ('django.db.models.fields.TextField', [], {})
        },
        u'jaguar.link': {
            'Meta': {'object_name': 'Link'},
            'archive': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Archive']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jaguar.Customer']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NEW'", 'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'014127a5-8e7c-491e-8928-680453e3a186'", 'max_length': '36', 'db_index': 'True'})
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
            'history': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
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