# Ler o salário do funcionário
salario = float(input())

# Definir os intervalos e percentuais de reajuste
if salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

# Calcular o valor do aumento e o novo salário
reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste

# Imprimir os resultados conforme especificado
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")