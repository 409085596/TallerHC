from math import *

def MedidaHipotenusa(a,b):
    c = sqrt(a**2 + b**2)
    return c

def zonaCirculo(x,y):
    valor = False
    if MedidaHipotenusa(x-15,y-20) < 10:
        valor = True
    return valor

def dianaCirculo(x,y):
    if x<5 or x>25:
        if y<10 or y>30:
            return(3)
        else:
            return(5)
    else:
        if y<10 or y>30:
            return(7)
        else:
            if zonaCirculo(x,y) == True:
                return(10)
            else:
                return(100)
