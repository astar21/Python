mi_archivo =open('prueba3.txt','a')
mi_archivo.write('SOY otro\n')
mi_archivo.writelines(['hola','mundo','aqui','estoy'])
lista = ['hola','mundo','aqui','estoy']
for p in lista:
    mi_archivo.writelines(p+'\n')

mi_archivo.close()