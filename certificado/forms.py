from django import forms
from .models import Alunos

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome_aluno', 'email', 'nome_curso','data_inicio']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }
