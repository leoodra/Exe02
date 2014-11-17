# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=27, verbose_name=b'Nome da Estrutura')),
                ('Ano', models.IntegerField(max_length=1, verbose_name=b'Ano de Cria\xc3\xa7\xc3\xa3o desta Estrutura')),
                ('Curso', models.ForeignKey(verbose_name=b'Curso', to='universidade.Curso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstruturaxDisciplinaxPeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Discipllina', models.ForeignKey(verbose_name=b'Disciplina', to='universidade.Disciplina')),
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='universidade.Estrutura', null=True)),
                ('Periodo', models.ForeignKey(verbose_name=b'Periodo', to='universidade.Periodo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=17, verbose_name=b'Nome da Turma')),
                ('Semestre', models.ForeignKey(verbose_name=b'Semestre', to='universidade.Semestre', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Tempo',
            field=models.IntegerField(max_length=1, verbose_name=b'Dura\xc3\xa7\xc3\xa3o (em anos)'),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='TipSem',
            field=models.IntegerField(max_length=1, verbose_name=b'O Semestre'),
        ),
    ]
