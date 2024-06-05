import numpy as np
import matplotlib.pyplot as plt

exponencial = np.random.exponential(scale=3/4, size=1000)

plt.hist(exponencial, bins=20, edgecolor='black')
plt.title('Distribución Exponencial')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()