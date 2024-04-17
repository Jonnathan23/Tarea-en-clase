import matplotlib.pyplot as plt

# Inicialización de variables
p = float(input("Ingrese la probabilidad de falla % ")) / 100
q = 1 - p
x = int(input("Numero de la prueba en la que ocurre el exito "))

# Cálculo de la probabilidad
px = p * (1 - p) ** (x - 1)

# Creación de la lista de valores de x
xValores = list(range(1, x + 1))

# Creación de la lista de probabilidades
probabilidades = [p * (1 - p) ** (i - 1) for i in xValores]

# Gráfico de barras
plt.bar(xValores, probabilidades, label=f'Probabilidad: {px*100:.2f}%')
plt.xlabel('Número de intento')
plt.ylabel('Probabilidad')
plt.title('Distribución de probabilidad binomial')
plt.legend()
plt.show()
