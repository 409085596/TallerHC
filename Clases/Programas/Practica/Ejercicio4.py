# -*- coding: utf-8 -*-
def malla():
    intervaloHorizontal= [-5+i*0.5 for i in range(21)]
    intervaloVertical= [-7+i*1.5 for i in range(10)]
    malla = []
    for x in intervaloHorizontal:
        for y in intervaloVertical:
            coordenada = []
            coordenada.append(x)
            coordenada.append(y)
            malla.append(coordenada)
    return malla
