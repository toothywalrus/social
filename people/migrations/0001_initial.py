# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialUser'
        db.create_table(u'people_socialuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'people', ['SocialUser'])

        # Adding M2M table for field groups on 'SocialUser'
        m2m_table_name = db.shorten_name(u'people_socialuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('socialuser', models.ForeignKey(orm[u'people.socialuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['socialuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'SocialUser'
        m2m_table_name = db.shorten_name(u'people_socialuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('socialuser', models.ForeignKey(orm[u'people.socialuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['socialuser_id', 'permission_id'])

        # Adding model 'Message'
        db.create_table(u'people_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_messages', to=orm['people.SocialUser'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_messages', to=orm['people.SocialUser'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'people', ['Message'])

        # Adding model 'Post'
        db.create_table(u'people_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['people.SocialUser'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'people', ['Post'])

        # Adding model 'Photo'
        db.create_table(u'people_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'people', ['Photo'])

        # Adding model 'Like'
        db.create_table(u'people_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('who', self.gf('django.db.models.fields.related.ForeignKey')(related_name='likes', to=orm['people.SocialUser'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'people', ['Like'])


    def backwards(self, orm):
        # Deleting model 'SocialUser'
        db.delete_table(u'people_socialuser')

        # Removing M2M table for field groups on 'SocialUser'
        db.delete_table(db.shorten_name(u'people_socialuser_groups'))

        # Removing M2M table for field user_permissions on 'SocialUser'
        db.delete_table(db.shorten_name(u'people_socialuser_user_permissions'))

        # Deleting model 'Message'
        db.delete_table(u'people_message')

        # Deleting model 'Post'
        db.delete_table(u'people_post')

        # Deleting model 'Photo'
        db.delete_table(u'people_photo')

        # Deleting model 'Like'
        db.delete_table(u'people_like')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.like': {
            'Meta': {'object_name': 'Like'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'who': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'likes'", 'to': u"orm['people.SocialUser']"})
        },
        u'people.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_messages'", 'to': u"orm['people.SocialUser']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_messages'", 'to': u"orm['people.SocialUser']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'people.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'people.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['people.SocialUser']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'people.socialuser': {
            'Meta': {'object_name': 'SocialUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['people']