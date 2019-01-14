# -*- coding: utf-8 -*-
'''Elías Jiménez Cruz 409085596
Tarea 02. En base a la tarea 1, consistente en escribir un programa que calculara la medida de la hipotenusa de un
triángulo rectángulo con las medidas de los catetos, mediante el teorema de Pitágoras, se va a escribir un nuevo programa
que realice el mismo procedimiento, sólo que mediante el uso de una función, con el propósito de que se pueda invocar
como biblioteca y se pueda ejecutar desde el shell de python para calcular diversas hipotenusas respecto a las medidas de
catetos distintos.'''

from math import *

def MedidaHipotenusa(a,b):
    c = sqrt(a**2 + b**2)
    return c

#Ejemplo para que el programa pueda imprimir un resultado por sí mismo:

print(MedidaHipotenusa(4,3))
