class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo =  modelo

    def info_veiculo(self):
        print(f"veiculo: {self.marca} {self.modelo}")

# classe base para navegacao
class Navegacao:
    def __init__(self, gps_marca):
        self.gps_marca = gps_marca

    def info_navegacao(self):
        print(f"sistema de navagacao: {self.gps_marca}")

# classe base para carga 
class Carga:
    def __init__(self, capacidade):
        self.capacidade = capacidade