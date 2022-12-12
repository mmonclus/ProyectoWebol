from django.contrib import admin
from .models import Servicio
# Register your models here.
#esto es para que me muestre los campos de update y create de forma solo lectura
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

#con esto lo gistro
admin.site.register(Servicio, ServicioAdmin)
