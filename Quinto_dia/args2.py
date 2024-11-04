def suma(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")
        total+= valor
        return total
suma(x=3,y=5,z=6)