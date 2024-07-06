# Ler o tempo gasto na viagem (em horas) e a velocidade média (em km/h)
tempo = int(input())
velocidade = int(input())

# Calcular a distância percorrida
distancia = tempo * velocidade

# Calcular a quantidade de litros necessária
litros = distancia / 12

# Imprimir a quantidade de litros com três casas decimais
print(f"{litros:.3f}")