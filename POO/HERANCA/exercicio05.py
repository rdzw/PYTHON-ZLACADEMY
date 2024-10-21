class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula

    @nome.setter
    def matricula(self):
        return self.__matricula
    
    def mostrar_info(self):
        print(f"Eu me chamo {self.nome} e minha matricula é {self.matricula}")

class Curso:
    def __init__(self, nome, codigo, alunos):
        self.__nome = nome
        self.__codigo = codigo
        self.__alunos = alunos[0]

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo

    @nome.setter
    def matricula(self):
        return self.__codigo
    
    @property
    def alunos(self):
        return self.__alunos

    @nome.setter
    def alunos(self):
        return self.__alunos
    

    def adicionar_alunos(self, aluno):
        aluno.append(self.alunos)

    def mostrar_alunos(self):
        print(f"alnunos matriculado são: {self.adicionar_alunos}")

class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__cursos = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        return self.__nome
    
    @property
    def cursos(self):
        return self.__cursos

    @cursos.setter
    def cursos(self):
        return self.__cursos
    

    def adicionar_curso(self, curso):
        curso.append(self.cursos)

    def mostrar_curso(self):
        print(f"os cursos foram {self.adicionar_curso}")