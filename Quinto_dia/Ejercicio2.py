def palabrasUnicas(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)


    unica = (set(lista))
    return (sorted(unica))


palabraGirada=palabrasUnicas('entretenido')
print(palabraGirada)









