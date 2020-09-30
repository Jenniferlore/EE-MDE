import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from sympy.parsing.sympy_parser import parse_expr

print ("Este programa implementará el método iterativo de Picard al PVI y' = t + y  y(0)=1")
t = sp.Symbol("t")
y = sp.Symbol("y")
y0 = input("Ingresa la función que se va a iterar: ")
f = parse_expr(y0)
n = int(input("Ingrese la cantidad de iteraciones a realizar: "))
if n <= 0:
    print ("Por favor ingresa un número no negativo.")
else:
    plt.figure()
    axis_t = np.linspace(-10, 10, 100)
    for i in range(1, n+1):
        F = sp.integrate(f + t, (t, 0, t))
        y = 1 + F
        f = y
        f_lamda = sp.lambdify(t, f, 'numpy')
        if i == 1 or i == n:
            axis_y = f_lamda(axis_t)
            leg="Iterada " + str(i)
            plt.plot(axis_t, axis_y, linestyle="dashed", label=leg)
    plt.title("Método iterativo de Picard aplicado a y' = t + y  y(0)=1")
    plt.xlabel("t")
    plt.ylabel("y(t)")


    Y = -(axis_t) - 1 + 2*np.exp(axis_t)
    plt.plot(axis_t, Y, label="Solución")
    plt.legend()
    plt.show()





