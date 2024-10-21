class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def mostrar_info(self):
        print(f"meu nome é {self.nome} e minha nacionalidade é {self.nacionalidade}")
    
class Livro:
    def __init__(self, titulo, isbn, ano_publicacao):
        self.titulo = titulo
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.autores = []

    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def motrar_info(self):
        print(f"meu livro é do titulo {self.titulo}, 
              com isbn {self.isbn} e foi publicado em {self.ano_publicacao}, escrito por {self.adicionar_autor}")

class Leitor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f"os leitores sao {self.nome} e sua idade é {self.idade}")


class Emprestimo(Leitor, Livro):
    def __init__(self, nome, titulo, data_emprestimo, data_devolucao):
        Leitor.nome = nome
        Livro.titulo = titulo
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def mostrar_info(self):
        print(f"o leito foi {self.nome},
              o livro foi {self.titulo},
              a data de emprestimo foi {self.data_emprestimo}, 
              e data de devolucao foi {self.data_devolucao}")

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []

    def adicionar_livros(self, livro):
        livro.append(self.livros)

    def realizar_emprestimo(self, livro, leitor, data_emprestimo):
        pass

    def mostrar_emprestimos(self):
        print(f"o emprestimo foi feito em {self.realizar_emprestimo}")


    def mostrar_livros(self):
        print(f"os livros são {self.livros}")