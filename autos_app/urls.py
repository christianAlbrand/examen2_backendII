from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path('agregar_auto/', views.agregar_auto, name='agregar_auto'),
    path('listar_autos/', views.listar_autos, name='listar_autos'),
]