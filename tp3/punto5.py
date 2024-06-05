import scipy.stats as stats

def calcular_intervalo_confianza(media, desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio):
    error_estandar = (mutiplicador_desvio * desviacion_estandar) / (tamanio_muestra ** 0.5) #calculo la raiz de la muestra
    margen_error = z * error_estandar
    intervalo_confianza = (media - margen_error, media + margen_error)
    return intervalo_confianza

mutiplicador_desvio = 2
media = 100
desviacion_estandar = 10
tamanio_muestra = 100
z = 2.58  # Para un intervalo de confianza del 99%
intervalo = calcular_intervalo_confianza(media, desviacion_estandar, tamanio_muestra, z, mutiplicador_desvio)
print("Intervalo de confianza:", intervalo)