# -*- coding: utf-8 -*-
from Ejercicio01 import determinaIgualdad

interruptor = True
while interruptor == True:
    a, b= input("\nDame dos listas para determinar si son iguales.\nTienen que estar separadas por un espacio, sin dejar espacios entre sus elementos:\n").split()
    a.pop(0);
    print (a)
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
