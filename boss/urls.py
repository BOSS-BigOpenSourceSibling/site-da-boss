from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('diversidade', views.diversidade, name='diversidade'),
    path('sisters', views.sisters, name='sisters'),
    path('materiais', views.materiais, name='materiais'),
    path('inscricao', views.inscricao, name='inscreva-se'),
]