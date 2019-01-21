def lmcd(datos):
    r=int(datos[0])%int(datos[1])
    while r != 0:
        datos[0]=datos[1]
        datos[1]=r
        r=int(datos[0])%int(datos[1])
    return datos[1]
