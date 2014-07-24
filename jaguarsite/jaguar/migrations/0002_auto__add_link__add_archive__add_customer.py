# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'jaguar_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('archive', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.Archive'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jaguar.Customer'])),
            ('expiryDate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'jaguar', ['Link'])

        # Adding model 'Archive'
        db.create_table(u'jaguar_archive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_path', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'jaguar', ['Archive'])

        # Adding model 'Customer'
        db.create_table(u'jaguar_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'jaguar', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'jaguar_link')

        # Deleting model 'Archive'
        db.delete_table(u'jaguar_archive')

        # Deleting model 'Customer'
        db.delete_table(u'jaguar_customer')


    models = {
        u'jaguar.archive': {
            'Meta': {'object_name': 'Archive'},
            'full_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'expiryDate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['jaguar']