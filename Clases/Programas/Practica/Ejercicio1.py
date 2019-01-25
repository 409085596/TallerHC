# -*- coding: utf-8 -*-
listaF=raw_input('''
Dame los grados Farenheit que deseas convertir a Celsius para comparar la
fórmula aproximada y la exacta. Deben estar separados por un espacio.
''').split()
print "Farenheit  Celsius  CelsiusA  Diferencia"
for F in listaF:
    print '%5d' %(float(F)),
    print '%10.2f' %(5*(float(F)-32)/9),
    print '%10.2f' %((float(F)-30)/2),
    print '%10.2f' %(5*(float(F)-32)/9-(float(F)-30)/2)
