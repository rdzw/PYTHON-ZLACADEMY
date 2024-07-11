# 10. Construa um algoritmo para calcular o IMC (Índice de Massa Corporal) de
# uma pessoa.


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)

print(f"Seu imc é de: {imc:.2f} kg/m²")