from django import forms
from .models import Alunos, CriarCertificado

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome_aluno', 'email', 'nome_curso','data_inicio']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }

class ValidacaoForm(forms.ModelForm):
	class Meta:
		model = CriarCertificado
		fields = ['id_certificado']
