# -*- coding: utf-8 -*-
def Fibonacci(n):
    datos = [0,1,1]
    contador = 3
    while contador <= n:
        datos[0] = datos[1]
        datos[1] = datos[2]
        datos[2] += datos[0]
        contador += 1
    return "El número correspondiente a la posición %d de la sucesión de Fibonacci es: %d" %(n,datos[2])
