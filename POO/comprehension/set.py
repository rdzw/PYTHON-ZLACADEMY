# Conjunto com os quadrados dos números de 0 a 10
quadrados_set = {x ** 2 for x in range(11)}
print("Conjunto de quadrados:", quadrados_set)

# Conjunto com as vogais em uma frase (sem duplicatas)
frase = "Programação em Python é divertida"
vogais_set = {char for char in frase if char in 'aeiouáéíóúãõAEIOUÁÉÍÓÚÃÕ'}
print("Conjunto de vogais:", vogais_set)
