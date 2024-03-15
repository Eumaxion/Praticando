from django.urls import path
from . import views

app_name= 'gerador'

urlpatterns = [
    path('', views.index, name='index'),
    path('atualizar/', views.number, name='atualizar')
]