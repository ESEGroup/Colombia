from __future__ import unicode_literals

from django.db import models

import uuid

departamentos_enum = (
	(1, 'DEL'),
	(2, 'Mecanica'),
)
status_enum = (
	(1, 'Disponivel'),
	(2, 'Alocado'),
	(3, 'Em Manutencao'),
	(4, 'Desativado'),
)
# Create your models here.
class Usuario(models.Model):
	"""Classe mae usuario"""
	nome = models.CharField(max_length=250)
	departamento = models.IntegerField(choices=departamentos_enum, default = 1)
	isChefe = models.BooleanField(default=False)

class Funcionario(Usuario):
	def __str__(self):
		return self.nome
	def criar():
		pass
class ChefeDeDepartamento(Usuario):
	def criar():
		pass

class Recurso(models.Model):
	"""Classe recurso, contendo todos os atributos de um recurso isolado"""
	nome = models.CharField(max_length=250, default='Nome do recurso...')
	referencia = models.CharField(max_length=50, default='Identificador unico do recurso', unique=True)
	departamento = models.IntegerField(choices=departamentos_enum, default=1)
	status = models.IntegerField(choices=status_enum, default=1)
	def criar():
		pass
	def listar(codigo):
		pass
	def desativar(codigo):
		pass
	def registrarDevolucao(codigo):
		pass
	def registrarAtraso(codigo):
		pass
	def registrarManutencao(codigo):
		pass
	def trocarStatus(codigo):
		pass
	def __str__(self):
		return self.nome

class Agendamento(models.Model):
	recurso = models.ForeignKey('Recurso', on_delete=models.CASCADE, null=True)
	responsavel = models.ForeignKey('Funcionario', on_delete=models.CASCADE, null=True)
	data_inicial = models.DateTimeField(auto_now=False)
	data_final = models.DateTimeField(auto_now=False)
	ativo = models.BooleanField(default=True)
	referencia = models.CharField(max_length=8, default=str(uuid.uuid4())[:8], editable = False)
	def criar():
		pass
	def geraID():
		return recurso.referencia + str(data_inicial)
	def cancelar():
		pass
	def listar():
		pass
	def __str__(self):
		return str(self.referencia)