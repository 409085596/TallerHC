# -*- coding: utf-8 -*-
from Ejercicio03 import lConversorFC

interruptor = True
while interruptor == True:
    datos =[0,0]
    datos[0], datos[1] = raw_input("Vamos a convertir los grados de una temperatura, dados en °C o °F, a °F o °C, respectivamente.\nPara ello ingresa los grados, seguido de un espacio y la letra C si son °C o F si son °F: ").split()
    print "%s" %(lConversorFC(datos))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
