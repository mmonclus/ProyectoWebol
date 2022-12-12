from django.contrib import admin
from .models import Pedido, LineaPedido
#  mdificado 2-12-22.
admin.site.register([Pedido, LineaPedido])