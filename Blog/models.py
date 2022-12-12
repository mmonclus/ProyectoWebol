from django.db import models
from django.contrib.auth.models import User

# Esta clase me da la categoria de los post 
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #esto lo agrega automaticamente 
    update=models.DateTimeField(auto_now_add=True)
    #esta clase me sirve para ponerle el nombre que yo quiera en la base de datos
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

# Esta clase me da  los post         
class Post(models.Model):
    titulo =models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    # cree la carpeta con ese nombre i meta las imgenes alli,no es nesesario imgen por eos null y blank en true
    imagen=models.ImageField(upload_to='blog', null=True,blank=True) 
    #esto para que si se borra el usurio se borren lo spost
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    #relaciono las categorias con los post
    categorias=models.ManyToManyField(Categoria, related_name='categorias')

    created=models.DateTimeField(auto_now_add=True) #esto lo agrega automaticamente 
    update=models.DateTimeField(auto_now_add=True)
    #esta clase me sirve para ponerle el nombre que yo quiera en la base de datos
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo
