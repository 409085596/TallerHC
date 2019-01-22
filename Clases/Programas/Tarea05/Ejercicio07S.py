    # -*- coding: utf-8 -*-
from Ejercicio07 import ldeterminador10

interruptor = True
while interruptor == True:
    datos = []
    datos.extend(raw_input("\nDame los diez números respecto a los cuales quieres calcular su promedio y el número mayor y menor.\nTienen que estar separados por un espacio: ").split())
    print ldeterminador10(datos)
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
