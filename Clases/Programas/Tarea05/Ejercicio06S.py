# -*- coding: utf-8 -*-
from Ejercicio06 import promedio10

interruptor = True
while interruptor == True:
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = raw_input("\nDame los 10 números que quieres promediar. Tienen que estar separados entre sí por un espacio:\n").split()
    print "El promedio es: %.2f\n" %(promedio10(int(a0), int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(a8), int(a9)))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
