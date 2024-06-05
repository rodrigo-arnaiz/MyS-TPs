import numpy as np
import matplotlib.pyplot as plt

numeros_aleatorios = np.random.randint(1, 101, 100)
print(numeros_aleatorios)

media = np.mean(numeros_aleatorios)
desvio_estandar = np.std(numeros_aleatorios)
varianza = np.var(numeros_aleatorios)

print("La media es:", media)
print("El desvío estándar es:", desvio_estandar)
print("La varianza es:", varianza)

plt.hist(numeros_aleatorios, bins=10, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()