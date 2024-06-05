import numpy as np
import matplotlib.pyplot as plt


def calcular_intervalo_confianza(media, desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio):
    error_estandar = (mutiplicador_desvio *
                      desviacion_estandar) / (tamanio_muestra ** 0.5)
    margen_error = z * error_estandar
    intervalo_confianza = (media - margen_error, media + margen_error)
    return intervalo_confianza


exponencial = np.random.exponential(scale=3, size=100)
exponencial2 = np.random.exponential(scale=3, size=1000)
exponencial3 = np.random.exponential(scale=3, size=10000)

media = np.mean(exponencial3)
desvio_estandar = np.std(exponencial3)
varianza = np.var(exponencial3)

tamanio_muestra = len(exponencial3)
mutiplicador_desvio = 2  # multiplicador de desvio de la consigna
z = 2.58  # Para un intervalo de confianza del 99%

print("La media es:", media)
print("El desvío estándar es:", desvio_estandar)
print("La varianza es:", varianza)
print("El tamaño de la muestra es:", tamanio_muestra)

intervalo = calcular_intervalo_confianza(
    media, desvio_estandar, tamanio_muestra, z, mutiplicador_desvio)
print("Intervalo de confianza:", intervalo)

# ver tema subplot (2,3,1) (2,3,2) (2,3,3)
plt.hist(exponencial, bins=20, edgecolor='black',
         label='Tamaño de muestra: 100')
plt.title('Histograma de Distribuciones Exponenciales')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

plt.hist(exponencial2, bins=20, edgecolor='black',
         label='Tamaño de muestra: 1000')
plt.title('Histograma de Distribuciones Exponenciales')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
plt.hist(exponencial3, bins=20, edgecolor='black',
         label='Tamaño de muestra: 10000')
plt.title('Histograma de Distribuciones Exponenciales')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
