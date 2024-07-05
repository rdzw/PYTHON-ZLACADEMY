# Ler os dados de entrada
descricao_inicio = input().split()
dia_inicio = int(descricao_inicio[1])

hora_inicio = input().split(':')
h1 = int(hora_inicio[0])
m1 = int(hora_inicio[1])
s1 = int(hora_inicio[2])

descricao_termino = input().split()
dia_termino = int(descricao_termino[1])

hora_termino = input().split(':')
h2 = int(hora_termino[0])
m2 = int(hora_termino[1])
s2 = int(hora_termino[2])

# Calcular a diferença de tempo em segundos
total_segundos_inicio = dia_inicio * 24 * 60 * 60 + h1 * 60 * 60 + m1 * 60 + s1
total_segundos_termino = dia_termino * 24 * 60 * 60 + h2 * 60 * 60 + m2 * 60 + s2

diferenca_segundos = total_segundos_termino - total_segundos_inicio

# Calcular dias, horas, minutos e segundos
dias = diferenca_segundos // (24 * 60 * 60)
diferenca_segundos %= (24 * 60 * 60)

horas = diferenca_segundos // (60 * 60)
diferenca_segundos %= (60 * 60)

minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60

# Imprimir o resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
