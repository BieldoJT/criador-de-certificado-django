from rest_framework import serializers
from certificado.models import Alunos

class AlunosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alunos
		fields = '__all__'
