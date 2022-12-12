#defino una variable global
def importe_total_carro(request):
    total=0
    # miro si el  key 'carro'  existe en exite en la sesión,
   # if 'carro' in request.session:
         #reviso que el usuario este autenticado
    if request.user.is_authenticated :
      for key, value in request.session["carro"].items():
          total = total +(float(value['precio']))
    else:
      total="Debes loguearte"      
    return{'importe_total_carro':total}       
