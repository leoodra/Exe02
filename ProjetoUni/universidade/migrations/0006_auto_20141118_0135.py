# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0005_auto_20141118_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estxdisxper',
            name='Nomeedp',
        ),
        migrations.AlterField(
            model_name='estxdisxper',
            name='Discipllina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='universidade.Disciplina', null=True),
        ),
    ]
