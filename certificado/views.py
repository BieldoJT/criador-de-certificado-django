from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Alunos, CriarCertificado
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse

def lista_alunos(request):
	alunos = Alunos.objects.all()
	return render(request, 'lista_alunos.html', {'alunos': alunos})


def adicionar_alunos(request):
	if request.method == "POST":
		form = AlunoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('lista_alunos')
	else:
		form = AlunoForm()
	
	return render(request, 'adicionar_aluno.html',{'form':form})


def atualizar_conclusao(request, aluno_id):
	aluno = get_object_or_404(Alunos, id=aluno_id)
	if request.method == "POST":
		data_conclusao = request.POST.get('data_conclusao')
		aluno.data_conclusao = data_conclusao
		aluno.save()
		return redirect('lista_alunos')
	return render(request, 'atualizar_conclusao.html', {'aluno': aluno})



def gerar_certificado(request, aluno_id):
	aluno = get_object_or_404(Alunos, id=aluno_id)

	
	criar_certificado = CriarCertificado.objects.create()


	html_string = render_to_string('criar_certificado.html', {
		'aluno': aluno,
		'criar_certificado': criar_certificado,
		'usuario': request.user,
	})


	pdf = HTML(string=html_string).write_pdf()
	
	response = HttpResponse(pdf, content_type='application/pdf')
	response['Content-Disposition'] = f'inline; filename="certificado_{aluno.nome_aluno}.pdf"'
	return response
