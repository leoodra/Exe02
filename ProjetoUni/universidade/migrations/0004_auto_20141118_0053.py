# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0003_auto_20141117_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='CargaHoraria',
            field=models.CharField(max_length=3, verbose_name=b'Carga Hor\xc3\xa1ria - (em hora)'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='NumPeriodo',
            field=models.CharField(max_length=2, verbose_name=b'N\xc3\xbamero do Per\xc3\xadodo'),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='TipSem',
            field=models.CharField(max_length=1, verbose_name=b'O Semestre', choices=[(b'1', b'1\xc2\xba Semestre'), (b'2', b'2\xc2\xba Semestre')]),
        ),
    ]
