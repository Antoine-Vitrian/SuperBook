from django.urls import path
from . import views
from .views import PostListView
from .views import PostCreateView

urlpatterns = [
    path('listaPosts/', views.lista_posts, name='lista_posts'),
    path('cbv-listaPosts/', PostListView.as_view(), name='cbv_lista_posts'),
    path('novo/', views.criar_post, name='criar_post'),
    path('posts/novo/', PostCreateView.as_view(), name='novo_post'),
]


