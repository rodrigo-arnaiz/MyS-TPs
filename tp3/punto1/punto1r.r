numeros_aleatorios <- sample(1:100, 100, replace = TRUE)

print(numeros_aleatorios)

media <- mean(numeros_aleatorios)
desvio_estandar <- sd(numeros_aleatorios)
varianza <- var(numeros_aleatorios)

print(paste("La media es:", media))
print(paste("El desvío estándar es:", desvio_estandar))
print(paste("La varianza es:", varianza))

hist(numeros_aleatorios, main = "Histograma", xlab = "Valor", ylab = "Frecuencia")