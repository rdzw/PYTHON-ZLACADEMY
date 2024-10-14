class Pessoa:
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    #medoto envelhecer
    def envelhecer(self, altura):
        if self.idade <= 21:
            print("a pessoa ira crescer 0,5 cm")
            total = altura + 0.05
            print(total)

    # medoto engoradar
    def engordar(self):
        pass

    # metodo emagracer
    def emagrecer(self):
        pass

    # metodo crescer
    def crescer(self):
        print("voce cresceu parabens")

pessoa = Pessoa('ana', 15, 68, 1.50)
print(pessoa.envelhecer(1.50))
print(pessoa.crescer())

