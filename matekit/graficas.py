import matplotlib.pyplot as plt
import numpy as np

def graficar_cuadratica():
    x = np.linspace(-10, 10, 400)
    y = x**2

    plt.plot(x, y)
    plt.title("Grafica de y = x^2")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()