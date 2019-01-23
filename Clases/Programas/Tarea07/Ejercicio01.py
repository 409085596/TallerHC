# -*- coding: utf-8 -*-
'''Programe una función que determine si dos listas son iguales.
Dos listas se consideran iguales si tienen igual longitud y sus elementos
en cada índice también lo son.'''

def determinaIgualdad(l1, l2):
    if len(l1) == len(l2):
        if l1 == [] and l2 == []:
            return "Si son iguales."
        else:
            if l1.pop() == l2.pop():
                return determinaIgualdad(l1, l2)
            else:
                return "No son iguales."
    else:
        return "No son iguales."
