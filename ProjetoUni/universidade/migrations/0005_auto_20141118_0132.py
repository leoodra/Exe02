# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0004_auto_20141118_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='estxdisxper',
            name='Nomeedp',
            field=models.CharField(max_length=7, null=True, verbose_name=b'Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='turma',
            name='Nome',
            field=models.CharField(max_length=17, null=True, verbose_name=b'Nome da Turma'),
        ),
    ]
