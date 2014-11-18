# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0009_auto_20141118_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplinaxaluno',
            old_name='TurmaAluno',
            new_name='Aluno',
        ),
        migrations.RenameField(
            model_name='disciplinaxaluno',
            old_name='TurmaDisciplina',
            new_name='Disciplina',
        ),
    ]
