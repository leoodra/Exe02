#coding:utf-8
from django.contrib import admin
from models import Coordenador
from models import Curso
from models import Semestre
from models import Aluno
from models import Horario
from models import Professor
from models import Disciplina
from models import Periodo
from models import Estrutura
from models import EstxDisxPer
from models import Turma
from models import TurmaxAluno
from models import TurmaxDisciplina
from models import DisciplinaxAluno
from models import TurxDisxHor

# Register your models here.

class CoordenadorAdmin(admin.ModelAdmin):
	list_display = ['Nome','Sexo','CPF','Telefone','Email','Cidade']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class CursoAdmin(admin.ModelAdmin):
	list_display = ['Nome','Tempo']
	list_filter = ['Nome','Tempo']
	search_fields = ['Nome','Tempo']
	save_as = True

class SemestreAdmin(admin.ModelAdmin):
	list_display=['TipSem']
	list_filter = ['TipSem']
	search_fields=['TipSem']
	save_as = True

class AlunoAdmin(admin.ModelAdmin):
	list_display = ['Nome','Sexo','CPF','Telefone','Email','Cidade']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class HorarioAdmin(admin.ModelAdmin):
	list_display = ['HoraEntrada','HoraSaida']
	save_as = True

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['Nome','Sexo','CPF','Telefone','Email','Cidade']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class DisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Nome','CargaHoraria']
	list_filter = ['Nome']
	search_field = ['Nome']

class PeriodoAdmin(admin.ModelAdmin):
	list_display = ['NumPeriodo']
	list_filter = ['NumPeriodo']
	search_fields = ['NumPeriodo']
	save_as = True

class  EstxDisxPerInline(admin.TabularInline):
	model = EstxDisxPer

class EstruturaAdmin(admin.ModelAdmin):
	list_display = ['Nome','Ano','Cuso']
	list_filter = ['Nome','Ano','Curso']
	list_display = ['Nome','Ano','Curso']
        inlines = [EstxDisxPerInline]
        save_as = True

class TurmaxAlunoAdmin(admin.TabularInline):
	model = TurmaxAluno

class TurmaAdmin(admin.ModelAdmin):
	list_display = ['Nome','Semestre']
	list_filter = ['Nome','Semestre']
	search_field = ['Nome','Semestre']
	save_as = True
	
class TurmaxDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Turma','EstDisPer']
 	lis_filter = ['Turma','EstDisPer']
	search_field = ['Turma','EstDisPer']
	save_as = True

class DisciplinaxAlunoAdmin(admin.ModelAdmin):
	list_display = ['TurmaAluno','TurmaDisciplina']
	list_filter = ['TurmaAluno','TurmaDisciplina']
	search_field = ['TurmaAluno','TurmaDisciplina']
	save_as = True

class TurxDisxHorAdmin(admin.ModelAdmin):
	list_display = ['TurmaxDisciplina','Professor','Horario']
	list_filter = ['TurmaxDisciplina','Professor','Horario']
	searc_fiels = ['TurmaxDisciplina','Professor','Horario']
	save_as = True


admin.site.register(Coordenador,CoordenadorAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Semestre,SemestreAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Horario,HorarioAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(Estrutura,EstruturaAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(TurmaxDisciplina,TurmaxDisciplinaAdmin)
admin.site.register(DisciplinaxAluno,DisciplinaxAlunoAdmin)
admin.site.register(TurxDisxHor,TurxDisxHorAdmin)



