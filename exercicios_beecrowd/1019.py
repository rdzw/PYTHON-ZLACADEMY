# Ler o valor inteiro N que representa o tempo em segundos
N = int(input())

# Calcular horas, minutos e segundos
horas = N // 3600
N = N % 3600
minutos = N // 60
segundos = N % 60

# Formatar a saída no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")
