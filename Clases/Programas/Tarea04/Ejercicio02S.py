# -*- coding: utf-8 -*-
from Ejercicio02 import AlturaPelota

interruptor = True
print "Aquí se muestra el ejemplo de calcular el(los) momento(s) en que se encuentra la pelota en h = 58.919467 cuando Vo = 34:\n"
print AlturaPelota(34, 58.919467)
while interruptor == True:
    a, b = raw_input("\nAhora vamos a calcular el(los) momento(s) en que una pelota se encuentra a una determinada altura,\ncuando es lanzada a una determinada velocidad. Para ello dame primero la velocidad en que es lanzada y\nseparada por un espacio dame la altura en que quieres que calcule el tiempo: ").split()
    print AlturaPelota(float(a), float(b))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
