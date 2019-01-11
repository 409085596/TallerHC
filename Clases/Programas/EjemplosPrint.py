# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

#Print out numbers with quotes "" such that we see the
#width of the field
print '"%d"' % i        #Comando %d imprime un entero.
print '"%5d"' % i       #Imprime un campo de cinco caracteres como mínimo. Si la variable tiene menos de cinco caracteres,
                        #deja espacios en blanco hacia la izquierda.
print '"%05d"' % i      #Situación anterior, sólo que en vez de dejar espacios en blanco, deja ceros

print '"%g"' % r        #Muestra el número en su expresión más corta, puede usar notación científica.
print '"%G"' % r        #Situación anterior
print '"%e"' % r        #Usa notación científica.
print '"%E"' % r        #Situación anterior.
print '"%20.2E"' % r    #Imprime un campo de 20 caracteres a semejanza de %xd, con dos decimales. Usa notación científica.
print '"%30g"' % r      #Imprime un campo de 30 caracteres a semejanza de %xd, con 5 decimales en la notación científica.
print '"%-30g"' % r     #Imprime un campo de 30 caracteres, dejando espacios en banco si es preciso a la derecha.
                        #Deja la variable en notación ceintífica.
print '"%-30.4g"' % r   #Situación anterior, sólo que utiliza cuatro caracteres para expresar la variable en notación científica.

print '%s' % i          #Imprime la variable pero transformada en cadena.
print '%s' % r          #Situación anterior, pero no muestra todo el valor de la variable.

print '%g %% of %.2f Euro is %.2f Euro' % \ # El doble porcentaje se usa para imprimir el símbolo de porcentaje, mientras que
      (5.1, 346, 5.1/100*346)               # %.2f se usa para dejar la variable con su valor entero y dos decimales.
