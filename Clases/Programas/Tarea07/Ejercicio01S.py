# -*- coding: utf-8 -*-
from Ejercicio01 import determinaIgualdad

interruptor = True
while interruptor == True:
    a, b= raw_input("\nDame dos listas para determinar si son iguales.\nTienen que estar separadas por un espacio, pero sin dejar espacios entre sus elementos:\n").split()
    a=a.replace("[",""); a=a.replace("]",""); b=b.replace("[",""); b=b.replace("]","")
    a=a.split(",") ; b=b.split(",")
    print (determinaIgualdad(a,b))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
