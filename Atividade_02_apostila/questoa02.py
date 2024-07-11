# 2. Escreva um programa para ler o ano de nascimento de uma pessoa e
# escrever uma mensagem que diga se ela poderá ou não votar este ano (não é
# necessário considerar o mês em que ela nasceu).

ano_nascimento = int(input("Digite seu ano de nascimento: "))

if ano_nascimento > 16 :
    print(f"Você poderá voltar esse ano")
else:
    print("Não poderá votar esse ano")