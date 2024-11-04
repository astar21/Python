from pathlib import Path,PureWindowsPath

carpeta = Path("C:/Users/Marco/Desktop/alternativa/otro_archivo.txt")

print(carpeta.stem)#nombre sin extension
print(carpeta.name)#nombre
print(carpeta.suffix)#extension
#Esta extension sirve para ver si exixte el directorio
if not carpeta.exists():
    print("este archivo no exixte")
else:
    print("genial exixte")()

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)