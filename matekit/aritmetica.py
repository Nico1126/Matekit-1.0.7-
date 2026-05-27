def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre 0"

    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    return a ** 0.5

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

def es_par(n):
    return n % 2 == 0

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True