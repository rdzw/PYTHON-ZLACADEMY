from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando números ímpares
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

# Elevando ao quadrado
quadrados_impares = list(map(lambda x: x ** 2, numeros_impares))

# Somando os resultados
soma_quadrados_impares = reduce(lambda x, y: x + y, quadrados_impares)

print("Soma dos quadrados dos números ímpares:", soma_quadrados_impares)
