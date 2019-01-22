def lsumaDeNumeros(n):
    datos = [0,0]
    while datos[0]<n:
        datos[0] += 1
        datos[1] += datos[0]
    return datos[1]
