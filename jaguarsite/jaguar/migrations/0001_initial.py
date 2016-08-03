# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'jaguar_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'jaguar', ['Customer'])

        # Adding model 'Archive'
        db.create_table(u'jaguar_archive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', max_length=2000)),
        ))
        db.send_create_signal(u'jaguar', ['Archive'])

        # Adding model 'Link'
        db.create_table(u'jaguar_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archive', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.Archive'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.Customer'])),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='de6ab2f0-6e89-4375-85af-c5f8d8892780', max_length=36, db_index=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='NEW', max_length=50)),
        ))
        db.send_create_signal(u'jaguar', ['Link'])

        # Adding model 'LinkHistory'
        db.create_table(u'jaguar_linkhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.Link'])),
            ('when', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('country', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('dns', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'jaguar', ['LinkHistory'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'jaguar_customer')

        # Deleting model 'Archive'
        db.delete_table(u'jaguar_archive')

        # Deleting model 'Link'
        db.delete_table(u'jaguar_link')

        # Deleting model 'LinkHistory'
        db.delete_table(u'jaguar_linkhistory')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '2000'}),
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
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'dcd91dc4-3453-4377-8ab1-4bf0cc62625a'", 'max_length': '36', 'db_index': 'True'})
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