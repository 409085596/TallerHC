from math import *
def H_eps(x,eps=0.01):
    if x < -eps:
        return 0
    elif -eps <= x <= eps:
        return "H eps = %.3f" %(0.5+x/(2*eps)*sin((pi*x)/eps))
    else:
        return 1

def prueba_H_eps():
    print H_eps(-5)
    print H_eps(-0.01)
    print H_eps(0)
    print H_eps(0.01)
    print H_eps(5)

prueba_H_eps()
