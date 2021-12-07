from django.contrib import admin

from tiendavirtual.administracion.models import Producto,Cliente

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)