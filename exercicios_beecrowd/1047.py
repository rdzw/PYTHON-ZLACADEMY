# Ler os valores em uma única linha e atribuir às variáveis
hi, mi, hf, mf = map(int, input().split())

# Calculando a duração do jogo em minutos
inicio_minutos = hi * 60 + mi
fim_minutos = hf * 60 + mf

# Calculando a diferença de tempo em minutos
duracao_minutos = fim_minutos - inicio_minutos

# Caso a duração seja negativa (jogo passa da meia-noite)
if duracao_minutos <= 0:
    duracao_minutos += 24 * 60  # Adicionar um dia em minutos (24 horas)

# Converter a duração de minutos para horas e minutos
duracao_horas = duracao_minutos // 60
duracao_minutos %= 60

# Imprimir o resultado no formato solicitado
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")