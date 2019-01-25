def recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * recursion(n-1)

n = input('''Dame el valor de n cuyo factorial quieres conocer: ''')
print "El factorial de %d es: " %(n),
print recursion(n)
