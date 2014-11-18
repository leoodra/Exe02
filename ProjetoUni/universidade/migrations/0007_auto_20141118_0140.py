# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0006_auto_20141118_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estxdisxper',
            old_name='Discipllina',
            new_name='Disciplina',
        ),
    ]
