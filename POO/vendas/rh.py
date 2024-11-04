def autenticar_acesso(func):
    def wrapper(self, *args, **kwargs):
        if self.cargo == "Gerente":
            return func(self, *args, **kwargs)
        else:
            print("Acesso negado: apenas gerentes podem aumentar salários.")
            return None
    return wrapper

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @autenticar_acesso
    def aumentar_salario(self, funcionario, percentual):
        funcionario.salario += funcionario.salario * (percentual / 100)
        print(f"Salário de {funcionario.nome} aumentado para {funcionario.salario:.2f}")
