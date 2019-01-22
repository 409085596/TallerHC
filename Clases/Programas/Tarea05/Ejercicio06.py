def lpromedio10(datos):
    suma = 0
    for c in datos:
        suma += float(c)
    return suma/(len(datos))
