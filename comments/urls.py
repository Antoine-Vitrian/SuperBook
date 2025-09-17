
from django.urls import path
from .views import detalhe_post # <--- ATENÇÃO NÃO ESQUECER! 

urlpatterns = [
    # outras rotas...
    path('<int:pk>/', detalhe_post, name='detalhe_post'),
]

