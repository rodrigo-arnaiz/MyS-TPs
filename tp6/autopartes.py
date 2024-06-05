import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Se cargan los datos de entrada
produccion_por_turno = 130
media_demanda = 150
desviacion_demanda = 25
puntos_de_reorden = [50, 60, 70, 80]
costo_mantenimiento_por_unidad = 70
dias_habiles_por_anio = 250
anios_a_simular = 30
inventario_inicial = 90

# Simula un anio
def simular_anio(punto_reorden):
    inventario = inventario_inicial
    turnos_adicionales = 0
    costo_total_mantenimiento = 0
    
    for _ in range(dias_habiles_por_anio):
        demanda_diaria = np.random.normal(media_demanda, desviacion_demanda)
        demanda_diaria = max(0, demanda_diaria)  # Asegurarse que la demanda no sea negativa
        
        # Producción del primer turno
        produccion = produccion_por_turno
        
        # Calcular el inventario al final del día
        inventario += produccion
        inventario -= demanda_diaria
        
        # Revisar si se necesita un turno adicional
        if inventario <= punto_reorden:
            turnos_adicionales += 1
            inventario += produccion_por_turno  # Producción del segundo turno
        
        # Calcular el costo de mantenimiento del stock
        costo_mantenimiento = inventario * costo_mantenimiento_por_unidad
        costo_total_mantenimiento += costo_mantenimiento
    
    return turnos_adicionales, costo_total_mantenimiento

# En resultados se almacenan los datos de las diferentes simulaciones
resultados = {}

# Calcula el intervalo de confianza del 95%
def calcular_intervalo_confianza(media, desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio):
    error_estandar = (mutiplicador_desvio *
                      desviacion_estandar) / (tamanio_muestra ** 0.5)
    margen_error = z * error_estandar
    intervalo_confianza = (media - margen_error, media + margen_error)
    return intervalo_confianza

for punto_reorden in puntos_de_reorden:
    turnos_adicionales_anuales = []
    costos_anuales = []

    for _ in range(anios_a_simular):
        turnos_adicionales, costo_mantenimiento = simular_anio(punto_reorden)
        turnos_adicionales_anuales.append(turnos_adicionales)
        costos_anuales.append(costo_mantenimiento)

    # Datos necesarios para el intarvalo de confianza
    promedio_turnos_adicionales = np.mean(turnos_adicionales_anuales)
    promedio_costo_anual = np.mean(costos_anuales)
    desviacion_estandar = np.std(costos_anuales)
    z = 1.96
    mutiplicador_desvio = 2
    intervalo_confianza = calcular_intervalo_confianza(promedio_costo_anual, desviacion_estandar, anios_a_simular, z, mutiplicador_desvio)
    resultados[punto_reorden] = {
        'Promedio de turnos adicionales por año': promedio_turnos_adicionales,
        'Costos anuales': costos_anuales,
        'Promedio de costo anual': promedio_costo_anual,
        'Intervalo de confianza de costo anual (95%)': intervalo_confianza
    }

# Mostrar los resultados
for punto_reorden, resultado in resultados.items():
    print(f"Punto de reorden: {punto_reorden} unidades")
    print(f"Promedio de turnos adicionales por año: {resultado['Promedio de turnos adicionales por año']:.2f}")
    print(f"Promedio de costo anual de mantenimiento de inventario: ${resultado['Promedio de costo anual']:.2f}")
    print(f"IC 95% de costo anual: (${resultado['Intervalo de confianza de costo anual (95%)'][0]:.2f}, ${resultado['Intervalo de confianza de costo anual (95%)'][1]:.2f})\n")

# Graficar histogramas de costos anuales
plt.figure(figsize=(12, 8))
for punto_reorden, resultado in resultados.items():
    plt.hist(resultado['Costos anuales'], bins=10, edgecolor='black', alpha=0.7, label=f'Punto de reorden: {punto_reorden}')

plt.title('Histogramas de costos anuales de mantenimiento de inventario')
plt.xlabel('Costo anual ($)/100000')
plt.ylabel('Frecuencia en años')
plt.legend(loc='upper right')
plt.show()