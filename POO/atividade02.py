class Cliente:
    #metodo inicialização
    def __init__(self,cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    # getter para cpf
    @property
    def cpf(self):
        return self.__cpf
    
    # setter para cpf
    @cpf.setter
    def set_cpf(self,valor):
        if valor < 0 :
            print("cpf invalivo")
        else:
            print("cpf invalido")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self):
        return self.__nome

###############################################

class Conta:
    # metodo de inicializacao
    def __init__(self,numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

###################inicio dos gatters e setters
    # gatter numero
    @property
    def numero(self):
        return self.__numero
    
    # setters numero
    @numero.setter
    def numero(self):
        return self.__numero
    

    @property 
    def saldo(self):
        return self.__saldo
    
    # gatters saldo 
    @saldo.getter
    def saldo(self):
        return self.__saldo

    
###################fim dos gatters e setters####################################

    def sacar(self,saldo):
        if saldo < 0:
            print("nao foi possivel sacar")
        else:
            print("saque realizado com sucesso !!!")

    def depositar(self, conta):
        if conta == True:
            print("Deposito realizado com sucesso")
        else:
            print("Nao foi possivel depositar")

    def transferir(self, saldo):
        if saldo < 0:
            print("transferencia não autorizada")
        else:
            print("transferencia autorizada")

    def mostrar_saldo(self):
        pass