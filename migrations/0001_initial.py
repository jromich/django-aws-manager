# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AWSServer'
        db.create_table(u'aws_manager_awsserver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aws_access_key', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('aws_secret_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('aws_region', self.gf('django.db.models.fields.CharField')(default='us-east-1', max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'aws_manager', ['AWSServer'])


    def backwards(self, orm):
        # Deleting model 'AWSServer'
        db.delete_table(u'aws_manager_awsserver')


    models = {
        u'aws_manager.awsserver': {
            'Meta': {'object_name': 'AWSServer'},
            'aws_access_key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'aws_region': ('django.db.models.fields.CharField', [], {'default': "'us-east-1'", 'max_length': '20'}),
            'aws_secret_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['aws_manager']