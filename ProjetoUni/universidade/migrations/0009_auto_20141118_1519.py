# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0008_turma_estrutura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmaxdisciplina',
            name='EstDisPer',
        ),
        migrations.AddField(
            model_name='turmaxdisciplina',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='universidade.EstxDisxPer', null=True),
            preserve_default=True,
        ),
    ]
