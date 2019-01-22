# -*- coding: utf-8 -*-
from Tarea06Integral import integral

interruptor = True
while interruptor == True:
    a, b, n = raw_input("\nCalcularemos un área aproximada bajo la curva de -6x3+5x2+2x+12 en base a un intervalo definido y dividido en un número finito de intervalos.\nPara ello, dame en orden el extremo izquierdo del intervalo, el extremo derecho y el número de intervalos en que quieres que se divida ese intervalo.\nTienen que estar separados por un espacio: ").split()
    print integral(float(a),float(b),int(n))
    interruptor = bool(raw_input("Si desea repetir el proceso ingrese cualquier caracter, de lo contrario presione enter: "))
