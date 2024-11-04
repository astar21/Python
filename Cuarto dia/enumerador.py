lista=['a','b','c']
indice =0

for item in lista:
    print(indice,item)
    indice +=1

for item in enumerate(lista):#hace lo mismo que lo de arriba
    print(item)
