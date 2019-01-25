# -*- coding: utf-8 -*-
from Ejercicio4 import malla
malla=malla()
listaF=[]
for punto in malla:
    listaF.append(float("%.5f" %(punto[0]**2/25-punto[1]**2/49)))
print "Esta es la lista que es resultado de evaluar la función en los puntos de malla:\n"
print listaF
