from .carro import Carro
from Tienda.models import Articulo
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request, producto_id):
    #creoa mi carro
    carro=Carro(request)
    #agrego el producto
    producto=Articulo.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    #redireciono a la tiendita
    return redirect("Tienda")


def eliminar_producto(request, producto_id):
    #creoa mi carro
    carro=Carro(request)
    #elimino el producto
    producto=Articulo.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    #redireciono a la tiendita
    return redirect("Tienda")   

def restar_producto(request, producto_id):
    #creoa mi carro
    carro=Carro(request)
    #elimino el producto
    producto=Articulo.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    #redireciono a la tiendita
    return redirect("Tienda")   

def limpiar_carro(request):   #def limpiar_carro(request, producto_id):
    #creoa mi carro
    carro=Carro(request)
    #limiop  el carro
    carro.limpiar_carro() 
    #redireciono a la tiendita
    return redirect("Tienda")       
