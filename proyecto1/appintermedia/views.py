
from django.http import HttpResponse
from django.shortcuts import render

from appintermedia.forms import ProductoFormulario

from .models import Producto

#Create your views here.

def producto(request):
    return render(request,'appintermedia/producto.html')

def donantes(request):
    return render(request,'appintermedia/donantes.html')

def sedes(request):
    return render(request,'appintermedia/sedes.html')

def entregas(request):
    return render(request,'appintermedia/entregas.html')

def inicio(request):
    return render(request,'appintermedia/inicio.html')


def productoFormulario(request):

    if request.method == 'POST':

        miFormulario= ProductoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            nombre=informacion['nombre']
            color=informacion['color']
            talla=informacion['talla']

            mi_producto=Producto(nombre=nombre,color=color,talla=talla)
            mi_producto.save()

            

            return render(request,'appintermedia/inicio.html')

    else:

        miFormulario=ProductoFormulario()

    return render(request,'appintermedia/productoFormulario.html',{"miForm":miFormulario}) 


def busquedaTalla(request):
    return render(request,'appintermedia/busquedaTalla.html')


def buscar(request):

    if request.GET['talla']:

        talla=request.GET['talla']
        producto= Producto.objects.filter(talla=talla)

        return render(request,'appintermedia/resultadoBusqueda.html' , {'producto':producto , 'talla':talla})

    else:
           
        return HttpResponse('no enviaste datos')