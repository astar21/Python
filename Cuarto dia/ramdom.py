from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = uniform(1,5)
print(aleatorio)

aleatorio=random()
print(aleatorio)


aleatorio=('azul','rojo','verde')
print(choice(aleatorio))

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)