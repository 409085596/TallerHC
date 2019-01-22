# -*- coding: utf-8 -*-
def integral(a,b,n):
    intervalos=[a+i*(b-a)/float(n) for i in range(n+1)]
    areaMinima=0
    areaMaxima=0
    areaTrapecio=0
    for i in range(len(intervalos)-1):
        valori = -6*intervalos[i]**3+5*intervalos[i]**2+2*intervalos[i]+12
        valorii = -6*intervalos[i+1]**3+5*intervalos[i+1]**2+2*intervalos[i+1]+12
        mayor,menor=0,0
        
        if valori > valorii:
            mayor = valori
            menor = valorii
        else:
            mayor = valorii
            menor = valori
        
        areaMinima += menor * (intervalos[i+1]-intervalos[i])
        areaMaxima += mayor * (intervalos[i+1]-intervalos[i])
        areaTrapecio += menor * (intervalos[i+1]-intervalos[i]) + (mayor-menor)*(intervalos[i+1]-intervalos[i])/2.0
        
    return "El área mínima es %.3f, el área máxima %.3f y el área de trapecios es %.3f" %(areaMinima,areaMaxima,areaTrapecio)
