# 3. Escreva um programa que verifique a validade de uma senha fornecida pelo
# usuário. A senha válida é o número 1234. Devem ser impressas as seguintes
# mensagens:
# ACESSO PERMITIDO caso a senha seja válida.
# ACESSO NEGADO caso a senha seja inválida.

numero = 1234

senha = int(input("Digite sua senha: "))

if(senha == numero):
    print(f"ACESSO PERMITIDO")
else:
    print(f"ACESSO NEGADO")