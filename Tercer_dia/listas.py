mi_lista=['a','b','c']
mi_lista2=['d','e','f']
mi_lista3=mi_lista+mi_lista2
print(type(mi_lista))
resultado = len(mi_lista)
print (mi_lista)
resultado = mi_lista[1]
print(resultado)
resultado = mi_lista[0:3]
print(resultado)
print(mi_lista+mi_lista2)
print(mi_lista3)
mi_lista3[0]='z' #sobreescribir en la lista
print(mi_lista3)
mi_lista3.append('g') #agrega elementos
print(mi_lista3)
mi_lista3.pop() #elemina ultimo elemento elementos
print(mi_lista3)
mi_lista3.pop(0) #elimina por posicion elementos
print(mi_lista3)
eleminado=mi_lista3.pop(0) #guardar el elemento en variable
print(eleminado)
lista4 =['z','a','g']
print(lista4)
lista4.sort()#ordenar lista
print(lista4)
lista4.reverse()
print(lista4)#al reves