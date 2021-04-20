from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('busca', views.busca, name='busca'),
    path('<int:disco_id>', views.detalhes, name='detalhes')
]
