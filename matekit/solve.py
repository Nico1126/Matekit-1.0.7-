import ast


# =========================
# MOTOR INTERNO
# =========================

def _eval(node):
    """
    Evalúa un AST y devuelve:
    (resultado, pasos)
    """

    # -------------------------
    # NÚMEROS
    # -------------------------
    if isinstance(node, ast.Constant):
        return node.value, []

    # Compatibilidad con versiones antiguas
    if getattr(ast, "Num", None) and isinstance(node, ast.Num):
        return node.n, []

    # -------------------------
    # OPERACIONES BINARIAS
    # -------------------------
    if isinstance(node, ast.BinOp):

        left, steps_left = _eval(node.left)
        right, steps_right = _eval(node.right)

        steps = steps_left + steps_right

        # SUMA
        if isinstance(node.op, ast.Add):
            result = left + right
            steps.append(f"{left} + {right} = {result}")
            return result, steps

        # RESTA
        if isinstance(node.op, ast.Sub):
            result = left - right
            steps.append(f"{left} - {right} = {result}")
            return result, steps

        # MULTIPLICACIÓN
        if isinstance(node.op, ast.Mult):
            result = left * right
            steps.append(f"{left} × {right} = {result}")
            return result, steps

        # DIVISIÓN
        if isinstance(node.op, ast.Div):
            result = left / right
            steps.append(f"{left} ÷ {right} = {result}")
            return result, steps

        # POTENCIA
        if isinstance(node.op, ast.Pow):
            result = left ** right
            steps.append(f"{left} ^ {right} = {result}")
            return result, steps

    # -------------------------
    # OPERADORES UNARIOS
    # -------------------------
    if isinstance(node, ast.UnaryOp):

        value, steps = _eval(node.operand)

        if isinstance(node.op, ast.USub):
            result = -value
            steps.append(f"-({value}) = {result}")
            return result, steps

        if isinstance(node.op, ast.UAdd):
            return value, steps

    raise ValueError("Unsupported expression")


# =========================
# SOLVE (solo resultado)
# =========================

def solve(expr):
    """
    Devuelve solo el resultado numérico.
    """
    tree = ast.parse(expr, mode="eval")
    result, _ = _eval(tree.body)
    return result


# =========================
# EXPLAIN (pasos + resultado)
# =========================

def explain(expr):
    """
    Devuelve pasos explicados + resultado final.
    """
    tree = ast.parse(expr, mode="eval")
    result, steps = _eval(tree.body)

    if not steps:
        steps = ["No intermediate steps"]

    return "\n".join([
        "MATEKIT EXPLANATION",
        "-------------------",
        f"Expression: {expr}",
        "",
        "Steps:",
        *[f"- {s}" for s in steps],
        "",
        f"Final Result: {result}"
    ])