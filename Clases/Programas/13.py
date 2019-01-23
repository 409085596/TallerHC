# -*- coding: utf-8 -*-
def fib(n): #Calcula el n término de la sucesión de Fibonacci con n natural.
    if n>2:
        return fib(n-1)+fib(n-2)
    else:
        return 1

def suma(n):
    if n==1:
        return 1
    else:
        return n+suma(n-1)

def printR(l):
    if len(l) > 1:
        return str(l.pop(0)) + ", " + printR(l)
    else:
        if len(l) == 1:
            return str(l.pop())
        else:
            return ""

def printr(l):
    if l:
        print l[0],
        printr(l[1:])
    else:
        None
