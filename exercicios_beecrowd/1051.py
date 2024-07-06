# Lendo o valor do salário
salario = float(input())

# Definindo as faixas e taxas de imposto
if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        imposto = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto = 1000.00 * 0.08 + (salario - 3000.00) * 0.18
    else:
        imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28

    # Formatando a saída conforme requerido
    print(f"R$ {imposto:.2f}")
