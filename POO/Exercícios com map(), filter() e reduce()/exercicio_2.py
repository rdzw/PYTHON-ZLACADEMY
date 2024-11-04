# Lista de números inteiros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() para encontrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Números pares:", numeros_pares)
