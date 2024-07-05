# Inicializando contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Lendo os 5 valores inteiros
for i in range(5):
    valor = int(input())
    
    # Verificando se é par ou ímpar
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificando se é positivo ou negativo
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

# Imprimindo os resultados
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")