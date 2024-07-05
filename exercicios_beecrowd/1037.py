"""
 leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos 
 ([0,25], (25,50], (50,75], (75,100]) este valor se encontra
"""

valor = float(input("Digite um valor qualquer: "))

if valor >= 0 and valor <=25:
    print(f"Itervalo [0,25]")
elif valor >= 25 and valor <=50:
    print(f"Intervalo (25,50]")
elif valor >=50 and valor <=75:
    print(f"Intervalo (50,75]")
elif valor >= 75 and valor <=100:
    print(f"Intervalo (75,100]")
else:
    print("Fora de intervalo")