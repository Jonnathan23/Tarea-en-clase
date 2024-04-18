from matplotlib import pyplot as plt
from math import comb

# Inicialización de variables
N = int(input("Ingrese el numero total de la poblacion (N): "))
k = int(input("Ingrese el numero de exitos de la poblacion (k): "))
n = int(input("Ingrese el numero de la muestra (n): "))
x = int(input("Ingrese el numero de exitos de la muestra (x):"))

# Cálculo de la probabilidad hipergeométrica
px = ((comb(k, x)) * comb((N - k), (n - x))) / comb(N, n)

# Mostrar resultado
print(f'P(x) = {px*100:.3f} %')

