
from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home,name='Home'),
    #path('Tienda', views.tienda,name='Tienda'),
   # path('Contacto', views.Contacto,name='Contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#ledecimos que le agregue a urlpatterns los setineg

