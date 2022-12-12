from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo =models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='sevicios') # cree la carpeta con ese nombre i meta las imgenes alli
    created=models.DateTimeField(auto_now_add=True) #esto lo agrega automaticamente 
    update=models.DateTimeField(auto_now_add=True)
    #esta clase me sirve para ponerle el nombre que yo quiera en la base de datos
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'

    def __str__(self):
        return self.titulo
