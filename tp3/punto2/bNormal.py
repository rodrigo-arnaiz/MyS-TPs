import numpy as np
import matplotlib.pyplot as plt

normal = np.random.normal(0, 1, 1000)

plt.hist(normal, bins=20, edgecolor='black')
plt.title('Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()