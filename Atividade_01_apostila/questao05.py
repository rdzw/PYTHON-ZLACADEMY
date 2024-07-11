# 5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um
# algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir
# quantos litros ele conseguiu colocar no tanque.

preco_litro = float(input("Digite o preço litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

litros_colocados = valor_pagamento / preco_litro

print(f"Foi possivel colocar com {valor_pagamento:.2f}, {litros_colocados:.2f} litros no tanque !!!")