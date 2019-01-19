# -*- coding: utf-8 -*-
from Ejercicio02 import mcd

interruptor = True
while interruptor == True:
    a, b = raw_input("\nDame los dos números respecto a los cuales quieres calcular el MCD.\nTienen que estar separados por un espacio: ").split()
    print "El MCD entre %s y %s es: %d\n" %(a, b, mcd(int(a),int(b)))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
