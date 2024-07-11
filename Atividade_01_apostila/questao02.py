# 2. Faça um algoritmo para calcular quantas ferraduras são necessárias para
# equipar todos os cavalos comprados para um haras.


qtd_cavalos = int(input("Quantos cavalos seu Haras possui ?: "))

# cada cavalo possui quatro patas
qtd_total_ferraduras = qtd_cavalos * 4

print(f"A quantidade de ferraduras é {qtd_total_ferraduras} para todos os cavalos")