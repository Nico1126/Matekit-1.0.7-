import sys
import ast
import matekit


def parse_arg(arg):
    try:
        return ast.literal_eval(arg)
    except Exception:
        return arg


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  matekit <function> [args]")
        return

    func_name = sys.argv[1]

    try:
        func = getattr(matekit, func_name)
    except AttributeError:
        print(f"Function '{func_name}' not found")
        return

    args = [parse_arg(arg) for arg in sys.argv[2:]]

    try:
        result = func(*args)

        if result is not None:
            print(result)

    except TypeError as e:
        print(f"Argument error: {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()