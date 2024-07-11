"""
1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo
para ler as dimensões de um terreno e depois exibir a área do terreno.
"""

largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

area_terreno = comprimento * largura

print(f"A area do terreno é: {area_terreno:.0f} m² ")