from django.shortcuts import render
from .models import Articulo

# Create your views here.
def tienda (request):
    producto=Articulo.objects.all()

    return render(request,"tienda/Tienda.html",{"productos":producto})
    #return HttpResponse("Tienda")