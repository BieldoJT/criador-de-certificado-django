from django.db import models
import uuid

class Alunos(models.Model):
	nome_aluno = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	nome_curso = models.CharField(max_length=255)
	data_inicio = models.DateField()
	data_conclusao = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.nome_aluno

class CriarCertificado(models.Model):
	id_certificado = models.UUIDField(
		default=uuid.uuid1,
		editable=False,
		unique=True
	)
	criacao_certificado = models.DateTimeField(auto_now_add=True)
