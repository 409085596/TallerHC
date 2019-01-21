# -*- coding: utf-8 -*-
def ConversorFC(t, n):
    if n=="C":
        return "La temperatura en °F es: %.3f°F" %(t*1.8 + 32)
    elif n=="F":
        return "La temperatura en °C es: %.3f°C" %((t-32)/1.8)
    else:
        return "Lo siento, tipo de conversión no definida."
