from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando reduce() para encontrar o produto
produto = reduce(lambda x, y: x * y, numeros)

print("Produto de todos os números:", produto)
