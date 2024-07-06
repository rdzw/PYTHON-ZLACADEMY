# Ler os três números inteiros
num1, num2, num3 = map(int, input().split())

# Colocar os números em uma lista
nums = [num1, num2, num3]

# Ordenar a lista
nums_sorted = sorted(nums)

# Imprimir os números ordenados
print(nums_sorted[0])
print(nums_sorted[1])
print(nums_sorted[2])

# Imprimir uma linha em branco
print()

# Imprimir os números na ordem em que foram lidos
print(num1)
print(num2)
print(num3)