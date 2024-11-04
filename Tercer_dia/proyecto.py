#crear un programa que :
#1 te pida que escribas un texto
frase=input("Dime una frase")
letra3 = (input("Dime 1 letra"))
letra1 = (input("Dime otra letra"))
letra2 = (input("Dime una mas"))

#2 te pida cuntas veces aparece esa letra
cuenta1=frase.find(letra1)
cuenta2=frase.find(letra2)
cuenta3=frase.find(letra3)
print("vamamos a contar las letras ")
print(f"la letra {letra1} aparece {cuenta1} veces")
print(f"la letra {letra2} aparece {cuenta2} veces")
print(f"la letra {letra3} aparece {cuenta3} veces")
#3 te digs cuantas palabras tiene la frase
resultado = len(frase)
print(f" la frase tiene {resultado} caracteres")
#4 te diga cual es la primera y ultima letra
letra_primera =frase[0]
letra_iltims =frase[-1]
print(f" la primera letra es: {letra_primera} y la ultima es:  {letra_iltims}")
#5 ordene las palabras al reves

frase
texto_invertido=[]
texto_invertido.append(frase)
texto_invertido.reverse()
texto_invertido = ''.join(frase)
print(texto_invertido)
#6 te mire si aprace la palabra python
lista =[]
lista.append(frase)
esta = 'python' in lista
print(f"#6 El resultado de si esta python es {esta}")


