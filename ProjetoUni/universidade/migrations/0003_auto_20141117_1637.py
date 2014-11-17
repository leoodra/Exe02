# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidade', '0002_auto_20141117_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaxAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstxDisxPer',
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
            name='TurmaxAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluno', models.ForeignKey(verbose_name=b'Aluno', to='universidade.Aluno', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='universidade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaxDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EstDisPer', models.ForeignKey(verbose_name=b'Estrutura', to='universidade.EstxDisxPer', null=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='universidade.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurxDisxHor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Horario', models.ForeignKey(verbose_name=b'Hor\xc3\xa1rio Inicio da Aula', to='universidade.Horario', null=True)),
                ('Professor', models.ForeignKey(verbose_name=b'Professor', to='universidade.Professor', null=True)),
                ('TurmaxDisciplina', models.ForeignKey(verbose_name=b'Disciplina', to='universidade.TurmaxDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='estruturaxdisciplinaxperiodo',
            name='Discipllina',
        ),
        migrations.RemoveField(
            model_name='estruturaxdisciplinaxperiodo',
            name='Estrutura',
        ),
        migrations.RemoveField(
            model_name='estruturaxdisciplinaxperiodo',
            name='Periodo',
        ),
        migrations.DeleteModel(
            name='EstruturaxDisciplinaxPeriodo',
        ),
        migrations.AddField(
            model_name='disciplinaxaluno',
            name='TurmaAluno',
            field=models.ForeignKey(verbose_name=b'Aluno', to='universidade.TurmaxAluno', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinaxaluno',
            name='TurmaDisciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='universidade.TurmaxDisciplina', null=True),
            preserve_default=True,
        ),
    ]
