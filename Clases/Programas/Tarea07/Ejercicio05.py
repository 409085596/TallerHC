# -*- coding: utf-8 -*-
'''Diseñe  y  programe  un  algoritmo  recursivo  que  encuentre  la  salida
de  un laberinto, teniendo en cuenta que el laberinto se toma como entrada y
que  es  una  matriz  de  valores  True,  False,  (x,y),  (a,b),  donde  True
indica uno bstáculo;  False,  una  celda  por  la  que  se  puede  caminar;
(x,y),  el  punto donde comienza a buscarse la salida y (a,b), la salida del
laberinto.'''

def laberinto(matriz, e):
    try:
        if matriz[e[0]-1][e[1]] == False:
            matriz[e[0]][e[1]] = True
            return(laberinto(matriz, (e[0]-1,e[1])))
    except:
        pass
    try:
        if matriz[e[0]][e[1]+1] == False:
            matriz[e[0]][e[1]] = True
            return(laberinto(matriz, (e[0],e[1]+1)))
    except:
        pass
    try:
        if matriz[e[0]+1][e[1]] == False:
            matriz[e[0]][e[1]] = True
            return(laberinto(matriz, (e[0]+1,e[1])))
    except:
        pass
    try:
        if matriz[e[0]][e[1]-1] == False:
            matriz[e[0]][e[1]] = True
            return(laberinto(matriz, (e[0],e[1]-1)))
    except:
        pass
    return("La salida es: "+str(e))
