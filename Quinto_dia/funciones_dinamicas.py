def chequea_3_cifras(lista):
    otra=[]
    for n in lista:
        if n in range(100, 1000):
            otra.append(n)
            #return True
        else:
            pass

    return otra

lista=[555,99,1]
resultado=chequea_3_cifras(lista)
print(resultado)


