serie ="N-01"
match serie:
    case "N-01":
        print('NOKIA')
    case "N-02":
        print('MOTOROLA')
    case "N-03":
        print('SAMSUNG')

clinte={'nombre':'fede','edad':35,'sexo':'hombre'}
peli={'nombre':'matrix','tematica':'accion','ficha tecnica' :{'actor':'pepe','director':'juan'}}
elementos=[clinte,peli,'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,'edad':edad,'sexo':sexo}:
            print("Es un cliente")
            print(nombre, edad, sexo)
        case {'nombre':nombre,'tematica':tematica,'ficha tecnica' :{'actor':actor,'director':director}}:
            print('ES una pelicula')
            print(nombre,tematica,actor,director)
        case _:
            print('Nose nada')










