def suma_vectores(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def resta_vectores(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def producto_escalar(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))