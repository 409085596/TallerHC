# -*- coding: utf-8 -*-
from Ejercicio07 import determinador10

interruptor = True
while interruptor == True:
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = raw_input("\nDame los diez números respecto a los cuales quieres calcular su promedio y el número mayor y menor.\nTienen que estar separados por un espacio: ").split()
    print determinador10(float(a0),float(a1),float(a2),float(a3),float(a4),float(a5),float(a6),float(a7),float(a8),float(a9))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
