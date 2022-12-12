#from logging import error
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from carro.carro import Carro

class VRegistro(View):
    #esta es la encargada de mostrar el formulario
    def get(self, request):
        form=UserCreationForm()
        return render(request,'registro/registro.html', {"form":form})
    #gestion a el envio del formulario
    def post(self, request):
        #almaceno en el form tdoso los datos que lleno el usuario
        form=UserCreationForm(request.POST)
        #compruebo si el formulario es valido
        if form.is_valid():
           ususario=form.save()
           #logueo al nuevo usuario
           login(request,ususario)
           
           #lo redirecciono al Home
           return redirect('Home')
            #mensaje para el que sepa que fue encviado el pedido
           messages.success(request, "Bienvenido")
        else:
             #tengo que recorrer todos los errores que cometio el usuario
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'registro/registro.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    #bacio el carro 
    carro=Carro.limpiar_carro(request)
    return redirect('Home')


def logear(request):
    #si pulso el boton
    if request.method == "POST":
       form=AuthenticationForm(request, data=request.POST)
       if form.is_valid():
          nombre_usuario=form.cleaned_data.get("username")
          contra=form.cleaned_data.get("password")
          usuario=authenticate(username=nombre_usuario,password=contra)
          #verifico si autentico
          if usuario is not None:
             login(request,usuario)
             return redirect('Home')
          else:
               messages.error(request,"Usuario o clave invalida") 
    else:
          messages.error(request,"Usuario o clave invalida")                

    form=AuthenticationForm()
        
    return render(request,'login/login.html', {"form":form})