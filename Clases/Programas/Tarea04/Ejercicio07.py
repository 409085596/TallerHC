# -*- coding: utf-8 -*-
def determinador10(a1,a2,a3,a4,a5,a6,a7,a8,a9,a0):
    p = (a1+a2+a3+a4+a5+a6+a7+a8+a9+a0)/10.0
    menor = a1
    mayor = a1
    if a2<menor:
        menor = a2
    if a3<menor:
        menor = a3
    if a4<menor:
        menor = a4
    if a5<menor:
        menor = a5
    if a6<menor:
        menor = a6
    if a7<menor:
        menor = a7
    if a8<menor:
        menor = a8
    if a9<menor:
        menor = a9
    if a0<menor:
        menor = a0
        
    if a2>mayor:
        mayor = a2
    if a3>mayor:
        mayor = a3
    if a4>mayor:
        mayor = a4
    if a5>mayor:
        mayor = a5
    if a6>mayor:
        mayor = a6
    if a7>mayor:
        mayor = a7
    if a8>mayor:
        mayor = a8
    if a9>mayor:
        mayor = a9
    if a0>mayor:
        mayor = a0
    return "El promedio es %.2f, el número menor es %g y el mayor es %g." %(p,menor,mayor)
