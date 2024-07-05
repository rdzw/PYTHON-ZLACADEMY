# Produto 1
nome1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o preço do primeiro produto: "))
percentual1 = float(input("Digite o percentual de desconto para o primeiro produto: "))

preco_desconto1 = preco1 - (preco1 * percentual1 / 100)

# Produto 2
nome2 = input("Digite o nome do segundo produto: ")
preco2 = float(input("Digite o preço do segundo produto: "))
percentual2 = float(input("Digite o percentual de desconto para o segundo produto: "))

preco_desconto2 = preco2 - (preco2 * percentual2 / 100)

# Produto 3
nome3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input("Digite o preço do terceiro produto: "))
percentual3 = float(input("Digite o percentual de desconto para o terceiro produto: "))

preco_desconto3 = preco3 - (preco3 * percentual3 / 100)

# Exibir os resultados formatados
print(f"Produto 1: {nome1} - Preço com desconto: R$ {preco_desconto1:.2f}")
print(f"Produto 2: {nome2} - Preço com desconto: R$ {preco_desconto2:.2f}")
print(f"Produto 3: {nome3} - Preço com desconto: R$ {preco_desconto3:.2f}")

total_pagar = preco_desconto1 + preco_desconto2 + preco_desconto3
print(f"\nTotal a pagar pelos 3 produtos: R$ {total_pagar:.2f}")
