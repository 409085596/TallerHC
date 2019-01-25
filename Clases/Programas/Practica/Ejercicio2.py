# -*- coding: utf-8 -*-
n=input('''
Dame el valor de n, de donde calcularemos la suma del cuadrado de los primeros
n números: ''')
suma = 0
for i in range(1,n+1):
    suma += i**2
print "La suma de los primeros n números por nuestro método es: %d" %(suma)
print "La suma de los primeros n números por la fórmula es: %d" %(n*(n+1)*(2*n+1)/6)
