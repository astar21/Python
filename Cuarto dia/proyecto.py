#programa pregunta al usuario su nombre
#he pensado un numero del 1 al 100 y tienes 8 inentos para adivinarlo
#4 opcionnes de respuesta
#numero menora 1 y mayor a 100 reespuesta invalida
#si elige un numero menor le dira que es in correcto y que su numero e menor
#si es mayor lo mismo
#y si acierta ha acertado y cuantos intentos le ha tomado
from random import *
nombre_jugador = input('Dime tu nombre')
print(f'{nombre_jugador}  tienes 8 intentos para adivinar el numero que estara desde el 1 al 50 tienes 8 intemntos ')
numero = randint(1,50)
contador = 0
ganador =False
while contador <8:
    if ganador is False:
        numero_jugaor = int(input('Dime un numero'))
        if numero_jugaor==0 or numero_jugaor >50:
            print("pon bien los datos")
            continue
        else:
            if numero_jugaor < numero:
                print(f"El numero a adivinar es mas grande,te quedan {7 - contador} intentos")
                contador = contador + 1
                continue
            elif numero_jugaor > numero:
                print(f"El numero a adivinar es mas pequeño,te quedan {7 - contador} intentos")
                contador = contador + 1
                continue
            elif numero_jugaor == numero:
                print(f"El numero {numero} es correcto!!")
                ganador == True
            break

if contador ==8:
    print(f"Se te han acabado los intentos,as perido el numero era {numero}")
else:
    print(F"Has ganado y te has gastado {contador} intentos ")




