#Leia um valor inteiro correspondente à idade de uma pessoa em dias
idade = int(input("Digite sua idade em dias: "))

ano = idade // 365 
dias_acumulados = idade % 365
mes = dias_acumulados // 30
dias = dias_acumulados % 30

print(f"{ano} ano (s)")
print(f"{mes} mes (es)")
print(f"{dias} dia (s)")


