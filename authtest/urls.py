from  django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('produtos/', views.produtos, name='produtos'),
    path('', views.pagina_inicial, name='pagina inicial'),
    path('testeDB/', views.DBteste, name='DBteste')
]
