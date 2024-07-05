# Leitura dos valores de entrada
A, B, C = map(float, input("").split())

# Ordenar os valores em ordem decrescente
valores = sorted([A, B, C], reverse=True)
A, B, C = valores

# Verificar as condições e imprimir as classificações
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")