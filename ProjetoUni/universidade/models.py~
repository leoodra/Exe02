#coding:utf-8
from django.db import models

# Create your models here.

SEXO = [
	('F','Feminino'),
	('M','Masculino')
]

SEMESTRE = [
	('1','1º Semestre'),
	('2','2º Semestre')
]



class Coordenador(models.Model):
	Nome = models.CharField('Nome',max_length=57,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	CPF = models.CharField('CPF',max_length=14,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unicode__(self):
		return self.Nome

class Curso(models.Model):
	Nome = models.CharField('Nome Curso',max_length=70,unique=True,null=True)
	Tempo = models.IntegerField('Duração (em anos)',max_length=1)
	
	def __unicode__(self):
		return self.Nome

class Semestre(models.Model):
	TipSem = models.CharField('O Semestre',max_length=1,choices=SEMESTRE)
	DtSemi =models.DateField('Inicio do Semestre')
	DtSemf = models.DateField('Fim do Semestre')
	
	def __unicode__(self):
		return self.Nome

class Aluno(models.Model):
	Nome = models.CharField('Nome',max_length=57,unique=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO)
	CPF = models.CharField('CPF',max_length=14,unique=True)
	DtNas = models.DateField('Data Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=13,null=True)
	Email = models.EmailField('E-mail',max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=30,null=True)
	
	def __unicode__(self):
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
	
	def __unicode__(self):
		return self.Nome

class Disciplina(models.Model):
	Nome = models.CharField('Nome da Disciplina',max_length=57,unique=True)
	CargaHoraria = models.CharField('Carga Horária - (em hora)',max_length=3)
	
	def __unicode__(self):
		return self.Nome
		
class Periodo(models.Model):
	NumPeriodo = models.CharField('Número do Período',max_length=2)

	def __unicode__(self):
		return self.NumPeriodo

class Estrutura(models.Model):
	Nome = models.CharField('Nome da Estrutura',max_length=27)
	Ano = models.IntegerField('Ano de Criação desta Estrutura',max_length=1)
	Curso = models.ForeignKey(Curso,verbose_name="Curso",null=True)

	def __unicode__(self):
		return "%s - %s" % (self.Curso.Nome,self.Nome)

class EstxDisxPer(models.Model):
	Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	Discipllina = models.ForeignKey(Disciplina,verbose_name="Disciplina")
	
	def __unicode__(self):
		return "%s - %s - %s" %(self.Estrutura.Nome,self.Periodo.NumPeriodo,self.Disciplina.Nome)

class Turma(models.Model):
	Nome = models.CharField('Nome da Turma',max_length=17)
	Semestre = models.ForeignKey(Semestre,verbose_name="Semestre",null=True)

	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.Semestre.TipoSem)

class TurmaxAluno(models.Model):
	Aluno = models.ForeignKey(Aluno,verbose_name="Aluno",null=True)
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)

	def __unicode__(self):
		return "%s - %s" % (self.Aluno.Nome,self.Turma.Nome)

class TurmaxDisciplina(models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	EstDisPer = models.ForeignKey(EstxDisxPer,verbose_name="Estrutura",null=True)
	
	def __unicode__(self):
		return "%s - %s" %(self.Turma.Nome,self.EstxDisxPer.Disciplina.Disciplina.Nome)

class DisciplinaxAluno(models.Model):
	TurmaAluno = models.ForeignKey(TurmaxAluno,verbose_name="Aluno",null=True)
	TurmaDisciplina = models.ForeignKey(TurmaxDisciplina,verbose_name="Disciplina",null=True)

	def __unicode__(self):
		return"%s - %s" %(self.TurmaxAluno.Aluno.Aluno.Nome,self.TurmaDisciplina.Turma.Turma.Nome)

class TurxDisxHor(models.Model):
	TurmaxDisciplina = models.ForeignKey(TurmaxDisciplina,verbose_name="Disciplina",null=True)
	Professor = models.ForeignKey(Professor,verbose_name="Professor",null=True)
	Horario = models.ForeignKey(Horario,verbose_name="Horário Inicio da Aula",null=True)
	
	def __unicode(self):
		return"%s - %s - %s" % (self.TurmaDisciplina.EstxDisxPer.Disciplina.Disciplina.Nome,self.Professor.Nome,self.Horario.HoraEntrada)

		









