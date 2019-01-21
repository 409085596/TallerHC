# -*- coding: utf-8 -*-
def Fibonacci(n):
    a1 = 1
    a2 = 1
    contador = 3
    while contador <= n:
        a0 = a1
        a1 = a2
        a2 += a0
        contador += 1
    return "El número correspondiente a la posición %d de la sucesión de Fibonacci es: %d" %(n,a2)
