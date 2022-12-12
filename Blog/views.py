from django.shortcuts import render
from Blog.models import Post, Categoria


# Create your views here.
def blog (request):
    posts=Post.objects.all()
    return render(request,"blog/Blog.html", {"posts":posts})
    #return HttpResponse("Blog")

def categoria (request,categoria_id):
    categoria= Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html", {"categoria":categoria,"posts":posts})