# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0007_auto_20141118_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='Estrutura',
            field=models.ForeignKey(verbose_name=b'Estrutura', to='universidade.Estrutura', null=True),
            preserve_default=True,
        ),
    ]
