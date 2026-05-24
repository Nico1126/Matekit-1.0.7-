import math

def ecuacion_lineal(a, b):
    return -b / a

def bhaskara(a, b, c):
    d = b**2 - 4*a*c

    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)

    return x1, x2

def sistema_2x2(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1

    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det

    return x, y