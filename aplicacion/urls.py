
from django.urls import path, include
from .views import *


urlpatterns = [
   
    path('', home, name="home"),
    path('cliente/', clientes, name="cliente"),
    path('marca/', marcas, name="marca"),
    path('patente/', patentes, name="patente"),
    path('problema/', problemas, name="problema"),

    path('cliente_form/', clienteForm, name="cliente_form" ),
    path('cliente_form2/', clienteForm2, name="cliente_form2" ),

     path('buscar_cliente/', buscarCliente, name="buscar_cliente" ),
    path('buscar2/', buscar2, name="buscar2" ),
]