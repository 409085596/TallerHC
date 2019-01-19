# -*- coding: utf-8 -*-
v0 = 34
g = 9.81
t = 0
y = v0*t - 1.0/2*g*t**2
print 'La posición de la pelota en el t=%g es %.2f' %(t,y)
print 'Esto es una prueba para t=%05d' %t

'''Hay distintas formas de imprimir variables. %E es para formato científico, %s para cadena, %g para imprimir la variable en
su expresión más corta posible, %f para imprimir una variable en una expresión flotante, usualmente se usa de la forma %a.bf,
donde a es el número mímimo de caracteres a imprimir y b el número de decimales a imprimir. Si a no está determinado,
se imprime el valor de la variable sin alterar. También tenemos %e para formato científico de números pequeños,
%d para número enteros.'''
