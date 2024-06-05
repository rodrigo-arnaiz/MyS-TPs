import numpy as np
import matplotlib.pyplot as plt

uniforme = np.random.uniform(0, 1, 1000)

plt.hist(uniforme, bins=20, edgecolor='black')
plt.title('Distribución Uniforme')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()