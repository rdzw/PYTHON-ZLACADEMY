print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

# criando uma variavel que recebe um valor
palavra_Secreta = 'banana'
letras_acertadas = ['_','_','_','_','_','_']

# criando variaveis booleanas e uma acumuladora
acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while(not acertou and not enforcou):
    chute = input('Qual letra?')
    
    posicao = 0
    for letra in palavra_Secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1
        
    else:
        erros += 1
    
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas) 

if (acertou):
    print('você ganhou!!!')
else:
    print('você perdeu !!!')
print('Fim de jogo')