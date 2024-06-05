import numpy as np
import matplotlib.pyplot as plt

poisson = np.random.poisson(6, 1000)

plt.hist(poisson, bins=20, edgecolor='black')
plt.title('Distribución de Poisson')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()