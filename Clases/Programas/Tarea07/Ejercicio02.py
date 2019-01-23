# -*- coding: utf-8 -*-
'''Programe  una  función  que  reciba  una  matriz  de  enteros  y  devuelva
una tupla con la lista o vector de la suma de cada fila y otro vector con la
suma de cada columna.'''

def sumaFilasColumnas(m):
    if len(m[0]) == 0:

    else:
        sumaC = 0
        for c in m:
            sumaC += c[0]
        return(sumaFilasColumnas(m[1:])
