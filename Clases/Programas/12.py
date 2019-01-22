# -*- coding: utf-8 -*-
alumnos = []
alumnos.append([9,8,10,9])
alumnos.append([9])
alumnos.append([6,9,10,8,9,10,10,9])
for i in range(len(alumnos)):
    for j in range(len(alumnos[i])):
        calificacion = alumnos[i][j]
        print "%4d" % calificacion,
    print
print
for i in alumnos:
    for j in i:
        print "%4d" % j,
    print

[["Alumno1",[["Álgebra",[10,9,8,7]],["Cálculo",[10,9,8,7]],["Geometría",[9,8,7,6]]], ["Alumno2",["Álgebra",[10,9,8,7]],["Cálculo",[10,9,8,7]],["Geometría",[9,8,7,6]]], [["Alumno1",["Álgebra",[10,9,8,7]],["Cálculo",[10,9,8,7]],["Geometría",[9,8,7,6]]]]
