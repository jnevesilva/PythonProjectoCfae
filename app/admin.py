from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Docente, Acao, Turma, Sessoes, Inscritos


# Register your models here.
@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ["designacao", "modalidade", 'horas','caducidade', 'registo' ]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ["id","turma", "codigoacao", "datainicio", 'datafim', 'fechada']

@admin.register(Sessoes)
class SessoesAdmin(admin.ModelAdmin):
    list_display = ["codturma",  "sessao", "data", 'duracao', 'sumario', 'localformacao']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ["username", "nome", "grupo", 'agrupamento', 'telefone', 'formador']

@admin.register(Inscritos)
class Inscritos(admin.ModelAdmin):
    list_display = ["idturma", "idutilizador", 'confirmado','concluiu','classificacao']
