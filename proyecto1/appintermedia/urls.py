
from django.urls import path

from.views import buscar, busquedaTalla, donantes, entregas, inicio, producto, productoFormulario, sedes

urlpatterns = [
    path('',inicio,name='inicio'),
    path('donantes/',donantes,name='donantes'),
    path('entregas/',entregas,name='entregas'),
    path('producto/',producto,name='productos'),
    path('sedes/',sedes,name='sedes'),
    path('productoFormulario/',productoFormulario,name='productoFormulario'),
    path('busquedaTalla/',busquedaTalla,name='busquedaTalla'),
    path('buscar/',buscar,name='buscar'),
]
