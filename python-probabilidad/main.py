from scipy.stats import norm

# Parámetros de la distribución
media = 4
desviacion = 0.3
valor = 0.2

r = norm()

# Calculamos la probabilidad acumulada
probabilidad_acumulada = norm.cdf(valor, loc=media, scale=desviacion)
probabilidad_acumulada