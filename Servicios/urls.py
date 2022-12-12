from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.servicios,name='Servicios'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#ledecimos que le agregue a urlpatterns los setineg

