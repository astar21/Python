from  random import shuffle
#lista inicial
palistos=['-','--','---','----']
#funcion mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedir intemto
def probar_suerte():
    intento=''
    while intento not in ['1','2','3','4']:
        intento= input("Elige un numero del 1 al 4: ")
    return int(intento)
#funcion intento
def comprobar(lista,intento):
    if lista[intento-1]=='-':
        print("a lavar los platos")
    else:
        print("te as salvado")


    print(f"te a tocado{lista[intento-1]}")


mezcla=mezclar(palistos)
selecccion = probar_suerte()
comprobar(mezcla,selecccion)
