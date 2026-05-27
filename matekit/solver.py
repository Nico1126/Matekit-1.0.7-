from sympy import symbols, solve, sympify

def resolver(ecuacion):
    x = symbols('x')

    expr = sympify(ecuacion)

    resultado = solve(expr, x)

    return resultado