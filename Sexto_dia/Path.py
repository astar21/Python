from pathlib import Path
base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","sagrada familia.txt"))
guia2 =guia.with_name("la_pedrera.txt")
print(guia)
print(base)
print(guia2)
