# Média 1

# Leia 2 valores de ponto flutuante de dupla precisão A e B
n1 = float(input("\nDigite a primeira nota? "))
n2 = float(input("\nDigite a segunda nota? "))

# sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11)
p1 = 3.5
p2 = 7.5

#sempre por os parenteses para o calculo dar certo
#o python identifica com parenteses os primeiros calculos
media = (n1*p1 + n2*p2)/(p1+p2)
print(f"MEDIA = {media:.1f}")

