# -*- coding: utf-8 -*-
def lConversorFC(datos):
    if datos[1]=="C":
        return "La temperatura en °F es: %.3f°F" %(float(datos[0])*1.8 + 32)
    elif datos[1]=="F":
        return "La temperatura en °C es: %.3f°C" %((float(datos[0])-32)/1.8)
    else:
        return "Lo siento, tipo de conversión no definida."
