from  django.urls import path
from . import views
urlpatterns = [
    path('admin/produtos', views.cadastroprod, name='cadastroprodutos'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('produtos/', views.produtos, name='produtos'),
    path('', views.pagina_inicial, name='pagina inicial')
]
