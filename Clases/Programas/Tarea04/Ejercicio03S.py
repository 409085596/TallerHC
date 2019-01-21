# -*- coding: utf-8 -*-
from Ejercicio03 import ConversorFC

interruptor = True
while interruptor == True:
    a, b = raw_input("Vamos a convertir los grados de una temperatura, dados en °C o °F, a °F o °C, respectivamente.\nPara ello ingresa los grados, seguido de un espacio y la letra C si son °C o F si son °F: ").split()
    print "%s" %(ConversorFC(float(a), b))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
