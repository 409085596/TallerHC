from math import sqrt

def lAlturaPelota(datos):
    t1 = sqrt(float(datos[0])**2/9.81-2*float(datos[1]))/-sqrt(9.81) + float(datos[0])/9.81
    t2 = -sqrt(float(datos[0])**2/9.81-2*float(datos[1]))/-sqrt(9.81) + float(datos[0])/9.81
    if "%.2f" %(t1) == "%.2f" %(t2):
        return 'El tiempo del recorrido de la pelota en que la altura es %s m es: %.2f s.' %(datos[1], t1)
    else:
        return 'Los tiempos del recorrido de la pelota en que la altura es %s m es: %.2f s y %.2f s.' %(datos[1], t1, t2)
