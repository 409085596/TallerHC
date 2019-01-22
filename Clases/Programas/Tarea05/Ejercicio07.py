# -*- coding: utf-8 -*-
def ldeterminador10(datos):
    promedio = 0
    for c in datos:
        promedio += float(c)/len(datos)
    menor = float(datos[0])
    mayor = float(datos[0])
    for c in datos:
        if menor > float(c):
            menor = float(c)
    for c in datos:
        if mayor < float(c):
            mayor = float(c)
    return "El promedio es %.2f, el número menor es %g y el mayor es %g." %(promedio,menor,mayor)
