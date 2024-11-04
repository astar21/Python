##for
lista2 = ['marco','marta','pili','javi']
for nombre in lista2:
     if nombre.startswith('m'):
         print(f'{nombre} comienza por M')
     else:
         print(f'{nombre} no comienza por M')
### while
monedas = 5
while monedas > 0:
    print(f"temgo {monedas} monedas ")
    monedas -=1
else:
    print("no tengo mas monedas")

#oro ejemplo
respuesta='s'

while respuesta =='s':
    respuesta =input('Quieres seguir S/N ')
else:
    print('Gracias')

##
while respuesta =='s':
    pass
print('Hola')

####
nombre = input("tu nombre")
for letra in nombre:
    if letra =='r':
        break
    print(letra)
nombre = input("tu nombre")
for letra in nombre:
    if letra =='r':
        continue
    print(letra)