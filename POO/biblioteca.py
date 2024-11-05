class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def mostrar_info(self):
        print(f"Autor: {self.nome}, Nacionalidade: {self.nacionalidade}")


class Livro:
    def __init__(self, titulo, isbn, ano_publicacao):
        self.titulo = titulo
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.autores = []

    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def mostrar_info(self):
        print(f"Título: {self.titulo}, ISBN: {self.isbn}, Ano de Publicação: {self.ano_publicacao}")
        for autor in self.autores:
            autor.mostrar_info()


class Leitor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_emprestimos = []
        self.livros_emprestados = []

    def mostrar_info(self):
        print(f"Leitor: {self.nome}, Idade: {self.idade}")

    def registrar_emprestimo(self, emprestimo):
        self.historico_emprestimos.append(emprestimo)
        self.livros_emprestados.append(emprestimo.livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")


class Emprestimo:
    def __init__(self, leitor, livro, data_emprestimo, data_devolucao=None):
        self.leitor = leitor
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def mostrar_info(self):
        print(f"Leitor: {self.leitor.nome}, Livro: {self.livro.titulo}, Data de Empréstimo: {self.data_emprestimo}")
        if self.data_devolucao:
            print(f"Data de Devolução: {self.data_devolucao}")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def realizar_emprestimo(self, livro, leitor, data_emprestimo):
        if livro not in self.livros:
            print(f"O livro '{livro.titulo}' não está disponível para empréstimo.")
            return

        if len(leitor.livros_emprestados) >= 3:
            print(f"O leitor '{leitor.nome}' já atingiu o limite de 3 livros emprestados.")
            return

        emprestimo = Emprestimo(leitor, livro, data_emprestimo)
        leitor.registrar_emprestimo(emprestimo)
        self.emprestimos.append(emprestimo)
        self.livros.remove(livro)
        print(f"Empréstimo do livro '{livro.titulo}' realizado com sucesso.")

    def devolver_livro(self, leitor, livro, data_devolucao):
        for emprestimo in self.emprestimos:
            if emprestimo.leitor == leitor and emprestimo.livro == livro:
                emprestimo.data_devolucao = data_devolucao
                leitor.devolver_livro(livro)
                self.livros.append(livro)
                print(f"Livro '{livro.titulo}' devolvido com sucesso.")
                return
        print(f"O livro '{livro.titulo}' não estava emprestado para {leitor.nome}.")

    def mostrar_emprestimos(self):
        print("Empréstimos realizados:")
        for emprestimo in self.emprestimos:
            emprestimo.mostrar_info()

    def mostrar_livros(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            livro.mostrar_info()

    def gerar_relatorio(self):
        total_livros = len(self.livros) + len(self.emprestimos)
        livros_disponiveis = len(self.livros)
        livros_emprestados = len(self.emprestimos)
        print(f"Total de livros: {total_livros}")
        print(f"Livros disponíveis: {livros_disponiveis}")
        print(f"Livros emprestados: {livros_emprestados}")

# Criação de autores
autor1 = Autor("Machado de Assis", "Brasileiro")
autor2 = Autor("Jane Austen", "Inglesa")

# Criação de livros e adição de autores
livro1 = Livro("Dom Casmurro", "123456789", 1899)
livro1.adicionar_autor(autor1)

livro2 = Livro("Orgulho e Preconceito", "987654321", 1813)
livro2.adicionar_autor(autor2)

# Criação de leitores
leitor1 = Leitor("Alice", 25)
leitor2 = Leitor("Carlos", 30)

# Criação da biblioteca e adição de livros
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Realizar empréstimos
biblioteca.realizar_emprestimo(livro1, leitor1, "2024-11-05")
biblioteca.realizar_emprestimo(livro2, leitor2, "2024-11-05")

# Mostrar empréstimos e livros disponíveis
biblioteca.mostrar_emprestimos()
biblioteca.mostrar_livros()

# Devolver livro
biblioteca.devolver_livro(leitor1, livro1, "2024-11-12")

# Relatório
biblioteca.gerar_relatorio()
