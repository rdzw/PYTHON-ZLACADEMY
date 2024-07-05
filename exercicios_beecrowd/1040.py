# Ler as quatro notas
notas = input().split()
N1, N2, N3, N4 = map(float, notas)

# Pesos das notas
pesos = [2, 3, 4, 1]

# Calcular a média ponderada
media = (N1 * pesos[0] + N2 * pesos[1] + N3 * pesos[2] + N4 * pesos[3]) / sum(pesos)
print(f"Media: {media:.1f}")

# Verificar a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Ler a nota do exame
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Recalcular a média final
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")
