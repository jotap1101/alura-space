from django.urls import path
from apps.galeria.views import index, imagem, search, filter, criar_fotografia, editar_fotografia, excluir_fotografia

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>', imagem, name='imagem'),
    path('search/', search, name='search'),
    path('filter/<str:categoria>', filter, name='filter'),
    path('criar_fotografia/', criar_fotografia, name='criar_fotografia'),
    path('editar_fotografia/<int:id>', editar_fotografia, name='editar_fotografia'),
    path('excluir_fotografia/<int:id>', excluir_fotografia, name='excluir_fotografia'),
]