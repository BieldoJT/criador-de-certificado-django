from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
	path('add/', views.adicionar_alunos, name='adicionar_alunos'),
	path('update/<int:aluno_id>/', views.atualizar_conclusao, name='atualizar_conclusao'),
	path('certtificado/<int:aluno_id>/', views.gerar_certificado, name='gerar_certificado'),
	]
