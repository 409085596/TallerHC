from math import sqrt

def AlturaPelota(Vo, h):
    t1 = sqrt(2*h + (Vo**2)/9.81)/sqrt(9.81) + Vo/9.81
    t2 = -sqrt(2*h + (Vo**2)/9.81)/sqrt(9.81) + Vo/9.81
    if t1 == t2:
        return 'El tiempo del recorrido de la pelota en que la altura es %f m es: %.2f s.' %(h, t1)
    else:
        return 'Los tiempos del recorrido de la pelota en que la altura es %.2f m es: %.2f s y %.2f s.' %(h, t1, t2)
