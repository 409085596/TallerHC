from math import sqrt

def AlturaPelota(Vo, h):
    t1 = sqrt(Vo**2/9.81-2*h)/-sqrt(9.81) + Vo/9.81
    t2 = -sqrt(Vo**2/9.81-2*h)/-sqrt(9.81) + Vo/9.81
    if "%.2f" %(t1) == "%.2f" %(t2):
        return 'El tiempo del recorrido de la pelota en que la altura es %f m es: %.2f s.' %(h, t1)
    else:
        return 'Los tiempos del recorrido de la pelota en que la altura es %f m es: %.2f s y %.2f s.' %(h, t1, t2)
