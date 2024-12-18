from rest_framework.routers import DefaultRouter
from .views import AlunosViewSet

router = DefaultRouter()
router.register(r'alunos', AlunosViewSet)

urlpatterns = router.urls

