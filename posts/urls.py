from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('listaPosts/', views.lista_herois, name='lista_posts'),
    path('cbv-listaPosts/', PostListView.as_view(), name='cbv_lista_posts'),
    path('novo/', views.criar_post(), name='criar_post'),
]