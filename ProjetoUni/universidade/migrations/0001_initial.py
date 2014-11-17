# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('CPF', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('DtNas', models.DateField(null=True, verbose_name=b'Data Nascimento')),
                ('Telefone', models.CharField(max_length=13, null=True, verbose_name=b'Telefone')),
                ('Email', models.EmailField(max_length=100, null=True, verbose_name=b'E-mail')),
                ('Cidade', models.CharField(max_length=30, null=True, verbose_name=b'Cidade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('CPF', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('DtNas', models.DateField(null=True, verbose_name=b'Data Nascimento')),
                ('Telefone', models.CharField(max_length=13, null=True, verbose_name=b'Telefone')),
                ('Email', models.EmailField(max_length=100, null=True, verbose_name=b'E-mail')),
                ('Cidade', models.CharField(max_length=30, null=True, verbose_name=b'Cidade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=70, unique=True, null=True, verbose_name=b'Nome Curso')),
                ('Tempo', models.IntegerField(max_length=1, verbose_name=b'Dura\xc3\xa7\xc3\xa3o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome da Disciplina')),
                ('CargaHoraria', models.IntegerField(max_length=3, verbose_name=b'Carga Hor\xc3\xa1ria - (em hora)')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HoraEntrada', models.TimeField(verbose_name=b'Hor\xc3\xa1rio In\xc3\xadcio Aula')),
                ('HoraSaida', models.TimeField(verbose_name=b'Hor\xc3\xa1rio Fim Aula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NumPeriodo', models.IntegerField(max_length=2, verbose_name=b'N\xc3\xbamero do Per\xc3\xadodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(unique=True, max_length=57, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('CPF', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('DtNas', models.DateField(null=True, verbose_name=b'Data Nascimento')),
                ('Telefone', models.CharField(max_length=13, null=True, verbose_name=b'Telefone')),
                ('Email', models.EmailField(max_length=100, null=True, verbose_name=b'E-mail')),
                ('Cidade', models.CharField(max_length=30, null=True, verbose_name=b'Cidade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipSem', models.IntegerField(max_length=1, verbose_name=b'Escolha o Semestre')),
                ('DtSemi', models.DateField(verbose_name=b'Inicio do Semestre')),
                ('DtSemf', models.DateField(verbose_name=b'Fim do Semestre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
