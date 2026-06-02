PI = 3.1416

def area_circulo(r):
    return PI * r * r

def perimetro_circulo(r):
    return 2 * PI * r

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_esfera(r):
    return (4/3) * PI * (r ** 3)

def volumen_cilindro(r, altura):
    return PI * (r ** 2) * altura

def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

def hipotenusa(cateto1, cateto2):
    return (cateto1**2 + cateto2**2) ** 0.5
