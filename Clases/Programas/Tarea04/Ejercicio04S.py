# -*- coding: utf-8 -*-
from Ejercicio04 import Fibonacci

interruptor = True
while interruptor == True:
    a = input("\nCalcularemos el número de la sucesión de Fibonacci en un posición determinada. Dame esa posición:\n")
    print Fibonacci(a)
    print "\n"
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
