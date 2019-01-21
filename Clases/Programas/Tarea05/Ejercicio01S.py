# -*- coding: utf-8 -*-
from Ejercicio01 import lmcd

interruptor = True
while interruptor == True:
    datos = [0,0]
    datos[0], datos[1] = raw_input("\nDame los dos números respecto a los cuales quieres calcular el MCD.\nTienen que estar separados por un espacio: ").split()
    print "El MCD entre %s y %s es: %s\n" %(datos[0], datos[1], lmcd(datos))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
