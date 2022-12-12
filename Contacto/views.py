from django.shortcuts import render,redirect
from .forms import FormularioContacto

from django.core.mail import send_mail
def contacto (request):
    formurio_contacto=FormularioContacto(data=request.POST)
    if formurio_contacto.is_valid():
       formurio_contacto=formurio_contacto.cleaned_data #tengo la ingo guradad
       send_mail(formurio_contacto['nombre'],formurio_contacto['contenido'], formurio_contacto.get('emal',''),['monclus@gmail.com'], )
       return redirect("/Contacto/?valido")
       try:      
           email.send()
           return redirect("/Contacto/?valido")
       except:
            return redirect("/Contacto/?valido")


    return render(request,"contacto/Contacto.html",{'miformulario':formurio_contacto})
