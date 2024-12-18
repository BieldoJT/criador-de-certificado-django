from rest_framework.viewsets import ModelViewSet
from certificado.models import Alunos
from .serializers import AlunosSerializer

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
