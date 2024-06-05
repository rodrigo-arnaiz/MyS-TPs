import numpy as np
import matplotlib.pyplot as plt

uniforme = np.random.uniform(0, 1, 1000)
beta = 12

def transformar_uniforme_a_exponencial(uniforme, beta):
    exponencial = - beta * np.log(1 - uniforme)
    return exponencial

exponencial = transformar_uniforme_a_exponencial(uniforme, beta)
plt.hist(exponencial, bins=20, edgecolor='black')
plt.title('Distribución Tranformada')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()