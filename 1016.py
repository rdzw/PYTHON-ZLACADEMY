# Lê a distância (em quilômetros)
distancia_km = int(input("Digite a distância em quilômetros: "))

# Velocidades dos carros
velocidade_x_kmh = 60
velocidade_y_kmh = 90

# Calcula a velocidade relativa
velocidade_relativa_kmh = velocidade_y_kmh - velocidade_x_kmh

# Calcula o tempo necessário em horas
tempo_horas = distancia_km / velocidade_relativa_kmh

# Converte o tempo para minutos
tempo_minutos = tempo_horas * 60

# Exibe o resultado
print(f"{tempo_minutos:.0f} minutos")
