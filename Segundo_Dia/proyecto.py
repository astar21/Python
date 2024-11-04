#haz un programa que le diga aun trabajador que segun las ventas que tenga un 13% mas de sueldo

nombre = input("como te llamas? ")
venta_mensual = input("cuanto has vendido este mes?")
venta_mensual = int (venta_mensual)
comision = float (venta_mensual*13/100)
comision = round(comision,1)
sueldo_final = (venta_mensual + comision)
print(f"{nombre} tu comision es  {comision} euros y tu sueldo total es {sueldo_final} euros")
