# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AWSServer.login'
        db.add_column(u'aws_manager_awsserver', 'login',
                      self.gf('django.db.models.fields.CharField')(default='Administrator', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AWSServer.login'
        db.delete_column(u'aws_manager_awsserver', 'login')


    models = {
        u'aws_manager.awsserver': {
            'Meta': {'object_name': 'AWSServer'},
            'aws_access_key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'aws_region': ('django.db.models.fields.CharField', [], {'default': "'us-east-1'", 'max_length': '20'}),
            'aws_secret_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'default': "'Administrator'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['aws_manager']