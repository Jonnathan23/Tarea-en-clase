import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

miu = int(input("Ingrese la media (µ): "))
sigma = int(input("Ingre la desviacion estandar (σ): "))
x = int(input("Ingrese el valor a encontrar (x): "))
z = (x - miu) / sigma

print(f'El estandar z = {z:.3f}')

# Calcula la probabilidad acumulada usando la función de distribución acumulada (CDF)
probabilidad = norm.cdf(z)

print(f'La probabilidad acumulada hasta z = {z:.3f} es: {probabilidad*100:.5f} %')

# Gráfica de la distribución normal
xValores = np.linspace(miu - 4*sigma, miu + 4*sigma, 1000)
yValores = norm.pdf(xValores, miu, sigma)

plt.plot(xValores, yValores, label='Distribución Normal')
plt.scatter(x, norm.pdf(x, miu, sigma), color='red', label=f'P(z)={probabilidad*100:.5f} %')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Normal')
plt.legend()
plt.grid(True)
plt.show()
