# 7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram
# desde o início do ano. Esqueça a questão dos anos bissextos e considere
# sempre que um mês possui 30 dias.


ano = 365
dia_mes = 30

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))


dias_contados = (mes - 1) * dia_mes + dia

print(f"Se passaram {dias_contados} desde o inicio do ano")


