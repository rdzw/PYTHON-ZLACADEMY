# Leitura do valor inteiro N
N = int(input())

# Inicialização das variáveis para cada tipo de nota
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0

# Cálculo do número mínimo de notas
valor = N

if valor >= 100:
    notas_100 = valor // 100
    valor = valor % 100

if valor >= 50:
    notas_50 = valor // 50
    valor = valor % 50

if valor >= 20:
    notas_20 = valor // 20
    valor = valor % 20

if valor >= 10:
    notas_10 = valor // 10
    valor = valor % 10

if valor >= 5:
    notas_5 = valor // 5
    valor = valor % 5

if valor >= 2:
    notas_2 = valor // 2
    valor = valor % 2

if valor >= 1:
    notas_1 = valor // 1
    valor = valor % 1

# Impressão dos resultados
print(N)
print(f'{notas_100} nota(s) de R$ 100,00')
print(f'{notas_50} nota(s) de R$ 50,00')
print(f'{notas_20} nota(s) de R$ 20,00')
print(f'{notas_10} nota(s) de R$ 10,00')
print(f'{notas_5} nota(s) de R$ 5,00')
print(f'{notas_2} nota(s) de R$ 2,00')
print(f'{notas_1} nota(s) de R$ 1,00')