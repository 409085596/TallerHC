# -*- coding: utf-8 -*-
from Ejercicio05 import laberinto

interruptor = True
while interruptor == True:
    matriz= input('''
Vamos a avergiuar cuál es la salida de un laberinto formado por una matriz.
Para ello, dame primero una matriz boolenana, sin espacios entre los elementos,
cuyas filas y columnas formarán las celdas por las que pasará el camino. Si el
valor de la celda es True, se le considerará un bloque por el que no se
podrá pasar, si es False, se podrá pasar por ahí. Así, las celdas que tengan
el valor false deberán formar un camino entre las celdas True, pero sin que
alguna celda False toque lateralmente a más de otra celda False.
Así mismo, una vez ingresado el laberinto, presiona enter e ingresa en
forma de tupla las coordenadas de filas y columnas donde se ubicará la entrada
del laberinto, que será la celda donde se empezará a recorrer el camino hasta el
final. Para dar mayor realismo al ejercicio, procura que la celda de entrada y
la de salida sean adyacentes a los bordes de la matriz:
''')
    e=input()
    print laberinto(matriz,e)
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter,\nde lo contrario presione enter: "))
