#coding:utf-8
from django.db import models

# Create your models here.

SEXO = [
	('F','Feminino'),
	('M','Masculino')
]


class Coordenador(models.Model):
	Nome = models.CharField('Nome',max_length=57,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	CPF = models.CharField('CPF',max_length=14,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unique__(self):
		return self.Nome

class Curso(models.Model):
	Nome = models.CharField('Nome Curso',max_length=70,unique=True,null=True)
	Tempo = models.IntegerField('Duração',max_length=1)
	
	def __unique__(self):
		return self.Nome

class Semestre(models.Model):
	TipSem = models.IntegerField('Escolha o Semestre',max_length=1)
	DtSemi =models.DateField('Inicio do Semestre')
	DtSemf = models.DateField('Fim do Semestre')
	
	def __unique__(self):
		return self.Nome

class Aluno(models.Model):
	Nome = models.CharField('Nome',max_length=57,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	CPF = models.CharField('CPF',max_length=14,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unique__(self):
		return self.Nome

class Horario(models.Model):
		HoraEntrada = models.TimeField('Horário Início Aula')
		HoraSaida = models.TimeField('Horário Fim Aula')


class Professor(models.Model):
	Nome = models.CharField('Nome',max_length=57,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	CPF = models.CharField('CPF',max_length=14,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unique__(self):
		return self.Nome

class Disciplina(models.Model):
	Nome = models.CharField('Nome da Disciplina',max_length=57,unique=True)
	CargaHoraria = models.IntegerField('Carga Horária - (em hora)',max_length=3)

class Periodo(models.Model):
	NumPeriodo = models.IntegerField('Número do Período',max_length=2)





