from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import ClienteForm


# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/cliente.html", contexto)

def marcas(request):
    contexto = {'marcas': Marca.objects.all()}
    return render(request, "aplicacion/marca.html", contexto)

def patentes(request):
    contexto = {'patentes': Patente.objects.all()}
    return render(request, "aplicacion/patente.html", contexto)

def problemas(request):
    contexto = {'problemas': Problema.objects.all()}
    return render(request, "aplicacion/problema.html", contexto)

def clienteForm(request):
    if request.method == "POST":


        cliente = Cliente(nombre=request.POST['nombre'],
                        DNI=request.POST['DNI'],
                        email=request.POST['email']
                        )
    
        cliente.save()
        return HttpResponse("Se grabo con exito el cliente!")
    return render(request, "aplicacion/clienteForm.html")  

def clienteForm2(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_DNI = miForm.cleaned_data.get('DNI')
            cliente_email = miForm.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre,
                            DNI=cliente_DNI,
                            email=cliente_email)
            cliente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClienteForm()
    
    return render(request, "aplicacion/clienteForm2.html", {"form": miForm })  


def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {"clientes": clientes, 'titulo': f'Clientes que tiene como patron "{patron}"'}
        return render(request, "aplicacion/cliente.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")
        

