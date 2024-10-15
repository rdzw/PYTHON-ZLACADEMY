class Peixe:
    def nadar(self):
        print("Peixe nadando")

class Boi:
    def andar(self):
        print("Boi andando")

class PeixeBoi(Peixe, Boi):
    def __init__(self, nome):
        self.nome = nome

    def caracteristicas(self):
        print(f"{self.nome} é um peixe-boi.")

# instanciando a classe peixe boi
pb = PeixeBoi("Manfred")
pb.andar()
pb.nadar()
pb.caracteristicas()