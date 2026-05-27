import sys
import inspect
import matekit

def main():
    if len(sys.argv) < 2:
        print("Uso: matekit <funcion> [argumentos]")
        return

    nombre_funcion = sys.argv[1]

    # Verifica si la función existe
    if not hasattr(matekit, nombre_funcion):
        print(f"La funcion '{nombre_funcion}' no existe.")
        return

    funcion = getattr(matekit, nombre_funcion)

    # Verifica que sea función
    if not callable(funcion):
        print(f"'{nombre_funcion}' no es una funcion.")
        return

    try:
        # Convierte argumentos a float
        args = [float(arg) for arg in sys.argv[2:]]

        resultado = funcion(*args)

        print(resultado)

    except TypeError:
        print("Cantidad de argumentos incorrecta.")

    except ValueError:
        print("Los argumentos deben ser numeros.")

if __name__ == "__main__":
    main()