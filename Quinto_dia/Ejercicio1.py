def devolver_destinos(numero1,numero2,numero3):
    lista = [];
    lista.append(numero1)
    lista.append(numero2)
    lista.append(numero3)
    if sum(lista)>15:
        return (max(lista))
    elif sum(lista)<10:
        return (min(lista))
    elif sum(lista)>=10 or sum(lista)<=15:
        return(6)


resp =devolver_destinos(3,5,1)

print(resp)
    #return max(lista)
   #if sum(lista) >15:




#numero=devolver_destinos(5,4,7)
#for i in numero:
    #print(numero)



