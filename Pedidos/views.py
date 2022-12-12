from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages #para los mensages emergentes
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail



# Create your views here.
@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # vemos el carro
    lineas_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorro el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))
    LineaPedido.objects.bulk_create(lineas_pedido) # crea registros en BBDD en paquete
    #enviamos mail al cliente con el peedido que me hizo 
    # (tener en cuanta que el usuario debe tener registrada una direccion de email valida)<--corregir cuendo re gistra
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
     
    )
    #mensaje para el que sepa que fue encviado el pedido
    messages.success(request, "El pedido se ha creado correctamente")
  

    #bacio el carro 
    carro=Carro.limpiar_carro(request)
    return redirect('Home')

    #lo redirecciono a la tienda
    #return redirect('../Tienda')

    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="latiendita@micasilla.com"
     # to=a la dirección del destinatario
    to=kwargs.get("email_usuario") 
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)       
   
