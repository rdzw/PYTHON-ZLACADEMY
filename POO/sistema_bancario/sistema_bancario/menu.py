# menu.py

from conta import Conta, SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidaError

class Menu:
    def __init__(self):
        self.contas = []

    def criar_conta(self):
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        limite = float(input("Digite o limite da conta: "))
        nova_conta = Conta(titular, saldo, limite)
        self.contas.append(nova_conta)
        print(f"Conta de {titular} criada com sucesso!")
    
    def encontrar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        return None

    def menu_principal(self):
        while True:
            print("\n----- MENU -----")
            print("1. Criar Conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Sair")
            opcao = int(input("Escolha uma opção: "))

            match opcao:
                case 1:
                    self.criar_conta()
                case 2:
                    self.depositar()
                case 3:
                    self.sacar()
                case 4:
                    self.transferir()
                case 5:
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida!")

    def depositar(self):
        titular = input("Digite o nome do titular da conta: ")
        conta = self.encontrar_conta(titular)
        if conta:
            valor = float(input(f"Digite o valor para depositar na conta de {titular}: "))
            conta.depositar(valor)
        else:
            print(f"Conta de {titular} não encontrada.")

    def sacar(self):
        titular = input("Digite o nome do titular da conta: ")
        conta = self.encontrar_conta(titular)
        if conta:
            valor = float(input(f"Digite o valor para sacar da conta de {titular}: "))
            try:
                conta.sacar(valor)
            except SaldoInsuficienteError as e:
                print(e)
        else:
            print(f"Conta de {titular} não encontrada.")

    def transferir(self):
        titular_origem = input("Digite o nome do titular da conta de origem: ")
        conta_origem = self.encontrar_conta(titular_origem)
        if conta_origem:
            titular_destino = input("Digite o nome do titular da conta de destino: ")
            conta_destino = self.encontrar_conta(titular_destino)
            valor = float(input(f"Digite o valor para transferir da conta de {titular_origem}: "))
            try:
                conta_origem.transferir(valor, conta_destino)
            except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidaError) as e:
                print(e)
        else:
            print(f"Conta de {titular_origem} não encontrada.")
