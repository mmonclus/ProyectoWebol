class Carro:
    def __init__(self,request) :
        self.request= request # aca tenemos almacenada la peticion
        self.session= request.session #con esto tengo iniciada la session
        carro=self.session.get("carro") #construyo un carro para esta session
         #el carro es un diccionario 
        if not carro:
            carro=self.session["carro"]={}
            #self.session["carro"]={}
            self.session.modified=True
        #else:
        self.carro=carro
             
    #funcion me agrega articulos al carro
    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            
           self.carro[producto.id]={
             "producto_id":producto.id,
             "nombre": producto.nombre,
             "precio": str(producto.precio),
             "cantidad":1,
             "imagen":producto.imagen.url
           }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                   value["cantidad"]=value["cantidad"]+1 
                   value["precio"]=float (value["precio"])+producto.precio 
                   break
        self.guardar_carro()  
             
     #me guarda los cambios relizados en micarro
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
         
     #funcion para eliminar productos de mi carro
    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro.keys():
        #if producto.id in self.carro:
           del self.carro[producto.id]  
           self.guardar_carro()
            
     #funcion me saca un producto del carro
    def restar_producto(self, producto):
        #para cada clave valor que tengo en el carro busca el id del articulo que quiero quitar
        for key,value in self.carro.items():
            
            if key==str(producto.id):
               value["cantidad"]=value["cantidad"]-1 
               value["precio"]=float (value["precio"])-producto.precio 
               if value["cantidad"]< 1: #si la cantidad es menor que 1 lo tengo que sacar 
                  self.eliminar(producto)  #self.eliminar(self,producto)
               break
        self.guardar_carro()   

     #esta funcion me limpia por completo el carro
    def limpiar_carro(self):
         self.session["carro"]={}
         self.session.modified=True



