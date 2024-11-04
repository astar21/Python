



precios_cafe=[('capuchino',1.15),('Expreso',1.30),('cortado',2.10)]

for cafe,precio in precios_cafe:
    print(precio*0.45)


def cafe_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro =''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor= precio
            cafe_mas_caro= cafe
        else:
            pass

    return cafe_mas_caro,precio_mayor
cafe, precio =cafe_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} y su precio es {precio} ")

