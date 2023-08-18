from django.template import Template, Context
from django.http import HttpResponse
import datetime
from aplicacion.models import *
from random import randint

def bienvenida(request):
    return HttpResponse("Bienvenidos")

def bienvenida_html(request):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos auto</h1>
    <h2>taller sergio</h2>
    <h3>hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(response)

def saludar(request, nombre):
    response = f"hola, bienvenido {nombre} al curso de django"
    return HttpResponse(response)

def bienvenida_template(request):
    miHtml = open("C:/Users/migue/Desktop/tp3/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
