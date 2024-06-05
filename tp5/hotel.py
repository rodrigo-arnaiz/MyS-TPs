import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Tareas
def romper_huevos():
    return np.random.uniform(2, 4)

def revolver_huevos():
    return np.random.uniform(3, 6)

def cocinar_huevos():
    return np.random.uniform(2, 5)

def cortar_panes():
    return np.random.uniform(3, 6)

def preparar_tostadas():
    return np.random.uniform(2, 5)

def preparar_bebidas_calientes():
    return np.random.uniform(4, 8)

def preparar_bebidas_frias():
    return np.random.uniform(3, 7)

# Accesos
def acceso_superior():
    return romper_huevos() + revolver_huevos() + cocinar_huevos()

def acceso_medio():
    return cortar_panes() + preparar_tostadas()

def acceso_inferior():
    return preparar_bebidas_calientes() + preparar_bebidas_frias()

# Simulación de un solo proyecto
def simular_proyecto():
    tiempo_superior = acceso_superior()
    tiempo_medio = acceso_medio()
    tiempo_inferior = acceso_inferior()
    
    # Se identifica el acceso que tardo más
    max_tiempo = max(tiempo_superior, tiempo_medio, tiempo_inferior)
    if max_tiempo == tiempo_superior:
        acceso_mas_lento = 'superior'
    elif max_tiempo == tiempo_medio:
        acceso_mas_lento = 'medio'
    else:
        acceso_mas_lento = 'inferior'
    
    return tiempo_superior, tiempo_medio, tiempo_inferior, tiempo_superior + tiempo_medio + tiempo_inferior, acceso_mas_lento

# Realizar 30 experimentos de 100 corridas cada uno
num_experimentos = 30
num_corridas = 100

resultados_corridas = []
promedios_experimentos = []
accesos_mas_lentos = []

# Listas para calcular los tiempos por acceso
tiempos_acceso_superior = []
tiempos_acceso_medio = []
tiempos_acceso_inferior = []

# Iteraciones de las 30 experimentos de 100 corridas cada uno
for _ in range(num_experimentos):
    tiempos_corridas = [simular_proyecto() for _ in range(num_corridas)]
    for t in tiempos_corridas:
        tiempos_acceso_superior.append(t[0])
        tiempos_acceso_medio.append(t[1])
        tiempos_acceso_inferior.append(t[2])
        resultados_corridas.append(t[3])
        accesos_mas_lentos.append(t[4]) 
    promedios_experimentos.append(np.mean([t[3] for t in tiempos_corridas]))

# Promedio de tiempo de finalización del proyecto
promedio_general = np.mean(resultados_corridas)

# Calcula el intervalo de confianza del 99%
def calcular_intervalo_confianza(media, desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio):
    error_estandar = (mutiplicador_desvio *
                      desviacion_estandar) / (tamanio_muestra ** 0.5)
    margen_error = z * error_estandar
    intervalo_confianza = (media - margen_error, media + margen_error)
    return intervalo_confianza

# Datos necesarios para el intarvalo de confianza
desviacion_estandar = np.std(resultados_corridas, ddof=1)
mutiplicador_desvio = 2
z = 2.57
tamanio_muestra = len(resultados_corridas)
intervalo_confianza = calcular_intervalo_confianza(promedio_general,desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio)

# Se calcula el porcentaje de criticidad para cada acceso
criticidad_superior = np.mean(tiempos_acceso_superior) / promedio_general * 100
criticidad_medio = np.mean(tiempos_acceso_medio) / promedio_general * 100
criticidad_inferior = np.mean(tiempos_acceso_inferior) / promedio_general * 100

contador_accesos_lentos = Counter(accesos_mas_lentos)

# Resultados en consola
print(f"Tiempo promedio de finalización del proyecto: {promedio_general:.2f}")
print(f"Intervalo de confianza del 99%: {intervalo_confianza}")
print(f"Criticidad del acceso superior: {criticidad_superior:.2f}%")
print(f"Criticidad del acceso medio: {criticidad_medio:.2f}%")
print(f"Criticidad del acceso inferior: {criticidad_inferior:.2f}%")


print("Frecuencia de accesos más lentos:")
for acceso, frecuencia in contador_accesos_lentos.items():
    print(f"{acceso}: {frecuencia} veces")


# Grafica histogramas
plt.figure(figsize=(12, 6))

# Histograma de los tiempos de las 3000 corridas
plt.subplot(1, 2, 1)
plt.hist(resultados_corridas, bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribución de tiempos de finalización del proyecto (3000 corridas)')
plt.xlabel('Tiempo')
plt.ylabel('Frecuencia')

# Histograma de los promedios de los 30 experimentos
plt.subplot(1, 2, 2)
plt.hist(promedios_experimentos, bins=15, edgecolor='k', alpha=0.7)
plt.title('Distribución de los promedios de los experimentos (30 experimentos)')
plt.xlabel('Tiempo promedio')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

