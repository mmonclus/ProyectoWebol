from django.shortcuts import render, HttpResponse

from carro.carro import Carro
#from Servicios.models import Servicio

# tengo que cear una vista para cada paerte.
def home (request):
    #inocio carro
    carro=Carro(request)
    return render(request,"ProyectoWebApp/Home.html")






     
     
        