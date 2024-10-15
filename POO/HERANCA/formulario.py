class FormularioBase:
    def _init_(self, cpf, nome, dataNascimento):
        self.__cpf = cpf
        self.__nome = nome
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
class FormularioLogin(FormularioBase):
    def _init_(self, cpf, nome, dataNascimento, usuario, senha):
        super()._init_(cpf, nome, dataNascimento)
        self.__usuario = usuario
        self.__senha = senha

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha
    
class FormularioEndereco(FormularioBase):
    def _init_(self, cpf, nome, dataNascimento, cep, rua, numero, bairro, cidade, estado):
        super()._init_(cpf, nome, dataNascimento)
        self.__cep =  cep
        self.__rua =  rua
        self.__numero =  numero
        self.__bairro =  bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cep(self):
        return self.__cep
    
    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado
    
class FormularioContato(FormularioBase):
    def _init_(self, cpf, nome, dataNascimento, telefone, celular, email):
        super()._init_(cpf, nome, dataNascimento)
        self.__telefone = telefone
        self.__celular = celular
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def celular(self):
        return self.__celular
    
    @property
    def email(self):
        return self.__email
