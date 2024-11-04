# Dicionário que mapeia números de 0 a 10 para seus quadrados
quadrados_dict = {x: x ** 2 for x in range(11)}
print("Dicionário de quadrados:", quadrados_dict)

# Dicionário com números ímpares de 0 a 10 como chaves e seus cubos como valores
cubos_dict = {x: x ** 3 for x in range(11) if x % 2 != 0}
print("Dicionário de cubos de números ímpares:", cubos_dict)
