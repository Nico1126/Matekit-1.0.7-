import math

def calc():
    print("=== Matekit Calculator ===")
    print("Type 'exit' to quit")

    allowed = {}

    # Agrega funciones matemáticas
    for name in dir(math):
        if not name.startswith("_"):
            allowed[name] = getattr(math, name)

    while True:
        expr = input(">>> ")

        if expr.lower() == "exit":
            print("Goodbye!")
            break

        try:
            result = eval(expr, {"__builtins__": {}}, allowed)
            print(result)

        except Exception as e:
            print("Error:", e)