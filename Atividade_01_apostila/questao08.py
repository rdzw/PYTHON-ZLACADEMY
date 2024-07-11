# 8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e
# imprimir a sua média ponderada (as notas tem pesos respectivos de 1, 2 e 3).

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

#soma dos pesos = 6
media = (n1*1 + n2*2 + n3*3) / 6

print(f"A media ponderada é : {media:.2f}")