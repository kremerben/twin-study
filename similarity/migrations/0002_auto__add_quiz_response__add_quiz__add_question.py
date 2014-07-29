# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz_Response'
        db.create_table(u'similarity_quiz_response', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'similarity', ['Quiz_Response'])

        # Adding model 'Quiz'
        db.create_table(u'similarity_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'similarity', ['Quiz'])

        # Adding model 'Question'
        db.create_table(u'similarity_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('weight', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quiz', to=orm['similarity.Quiz'])),
        ))
        db.send_create_signal(u'similarity', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Quiz_Response'
        db.delete_table(u'similarity_quiz_response')

        # Deleting model 'Quiz'
        db.delete_table(u'similarity_quiz')

        # Deleting model 'Question'
        db.delete_table(u'similarity_question')


    models = {
        u'similarity.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quiz'", 'to': u"orm['similarity.Quiz']"}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'similarity.quiz': {
            'Meta': {'object_name': 'Quiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'similarity.quiz_response': {
            'Meta': {'object_name': 'Quiz_Response'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['similarity']