nome = input("Digite seu nome: ")
salario = int(input("Digite seu salario: "))

aumento = salario + (salario * 0.15)

print("\nOlá " + nome)
print("\nSeu aumento salarial é de : %.2f" % aumento)