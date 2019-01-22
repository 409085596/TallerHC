# -*- coding: utf-8 -*-
from Ejercicio06 import lpromedio10

interruptor = True
while interruptor == True:
    datos = []
    datos.extend(raw_input("\nDame los 10 números que quieres promediar. Tienen que estar separados entre sí por un espacio:\n").split())
    print "El promedio es: %.2f\n" %(lpromedio10(datos))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
