# Ler o valor do salário
salario = float(input())

# Verificar em qual faixa de imposto o salário se encaixa e calcular o imposto devido
if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        imposto = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto = 1000.00 * 0.08 + (salario - 3000.00) * 0.18
    else:
        imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28

    # Imprimir o valor do imposto de renda devido
    print(f"R$ {imposto:.2f}")