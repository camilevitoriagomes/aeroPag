from django.urls import path
from .views import TarifaCreate, TarifaUpdate, TarifaDelete, TarifaList

urlpatterns = [
    path('tarifas/', TarifaList.as_view(), name='listar-tarifas'),
    path('tarifas/criar/', TarifaCreate.as_view(), name='criar-tarifa'),
    path('tarifas/<int:pk>/edit/', TarifaUpdate.as_view(), name='editar-tarifa'),
    path('tarifas/<int:pk>/delete/', TarifaDelete.as_view(), name='deletar-tarifa'),
]