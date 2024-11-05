# conta.py

class SaldoInsuficienteError(Exception):
    def __init__(self, message="Saldo insuficiente para completar a operação."):
        self.message = message
        super().__init__(self.message)

class LimiteExcedidoError(Exception):
    def __init__(self, message="Valor da transferência excede o limite permitido."):
        self.message = message
        super().__init__(self.message)

class ContaDestinoInvalidaError(Exception):
    def __init__(self, message="A conta destino não é válida."):
        self.message = message
        super().__init__(self.message)

class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Você tentou sacar R${valor}, mas seu saldo é R${self.saldo}.")
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
    
    def transferir(self, valor, conta_destino):
        if valor > self.limite:
            raise LimiteExcedidoError(f"O valor de R${valor} excede o limite de R${self.limite}.")
        if not isinstance(conta_destino, Conta):
            raise ContaDestinoInvalidaError("A conta de destino fornecida não é válida.")
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente para transferir R${valor}. Saldo atual: R${self.saldo}.")
        
        self.saldo -= valor
        conta_destino.saldo += valor
        print(f"Transferência de R${valor} para {conta_destino.titular} realizada com sucesso.")
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

