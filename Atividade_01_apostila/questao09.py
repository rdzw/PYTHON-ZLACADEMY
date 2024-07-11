# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
# cada uma sendo vendida respectivamente por 10, 12 e 15 reais. Construa um
# algoritmo em que o usuário forneça a quantidade de camisetas pequenas,
# médias e grandes referentes a uma venda, e a máquina informe quanto será o
# valor arrecadado.

qtd_camisetas_p = int(input("Digite a quantidade de camisetas pequenas: "))
qtd_camisetas_m = int(input("Digite a quantidade de camisetas medias: "))
qtd_camisetas_g = int(input("Digite a quantidade de camisetas grandes: "))

valor_arrecadado = qtd_camisetas_p*10 + qtd_camisetas_m*12 + qtd_camisetas_g*15

print(f"O total arrecado foi de R$ {valor_arrecadado:.2f} reais")