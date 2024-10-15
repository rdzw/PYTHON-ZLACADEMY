class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    # getter
    @property
    def marca(self):
        return self.__marca
    
    # gatter
    @property
    def modelo(self):
        return self.__modelo
    
    # setter
    @marca.setter
    def marca(self):
        return self.marca

    # setter
    @modelo.setter
    def modelo(self):
        return self.modelo


    def informacao(self):
        print(f"{self.marca} é a marca.")
        print(f"{self.marca} é a marca.")

class Carro(Veiculo):
    # incluindo o atributo numero de portas
    def __init__(self, n_portas, modelo, marca):
        self.n_portas = n_portas

    def informacao_completa(self):
        print(f"{self.marca} é a marca.")
        print(f"{self.marca} é a marca.")
        print(f"{self.n_portas} é o numero de portas.")


car = Carro(5,'corola', 'honda')
car.informacao_completa()
    
