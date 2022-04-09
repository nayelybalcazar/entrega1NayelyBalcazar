from atexit import register
from django.contrib import admin

from .models import Producto,Donantes,Sedes,Entregas

# Register your models here.

admin.site.register(Producto)
admin.site.register(Donantes)
admin.site.register(Sedes)
admin.site.register(Entregas)
