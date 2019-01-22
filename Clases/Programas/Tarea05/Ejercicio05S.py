# -*- coding: utf-8 -*-
from Ejercicio05 import lsumaDeNumeros

interruptor = True
while interruptor == True:
    a = input("Vamos a calcular la suma de los primeros n números naturales. Dame el valor de n: ")
    print "La suma de los primeros %d números es: %d" %(a, lsumaDeNumeros(a))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
