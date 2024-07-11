# 3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma
# quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa
# R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos
# pães e broas (juntos), e quanto deve guardar numa conta de poupança (10%
# do total arrecadado). Você foi contratado para fazer os cálculos para o dono.
# Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e
# de broas, e depois calcular os dados solicitados.

qtd_paes = float(input("Qual a quantidade de paes: "))
qtd_broas = float(input("Qual a quantidade de broas: "))

# paes = 0.12
# broa = 1.50

total_vendas = (qtd_paes*0.12) + (qtd_broas*1.50)
conta_poupança = total_vendas * 0.10

print(f"O total de vendas foi: {total_vendas:.2f} de pães e broas")
print(f"O dono deve guardar {conta_poupança:.2f} na conta poupança")