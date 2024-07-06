#Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A = float(input("DIGITE"))
B = float(input("DIGITE"))
C = float(input("DIGITE"))

#A seguir, calcule a média do aluno, sabendo que a 
#nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5
A*=2
B*=3
C*=5 
media = (A+B+C)/10

#Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo
print(f"MEDIA = {media:.1f}")
