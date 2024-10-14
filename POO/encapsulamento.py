class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Por padrão, o livro é disponível
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")
    
    def mostrar_info(self):
        status = "disponível" if self.disponivel else "emprestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}")

class Livraria:
    def __init__(self):
        #uma lista de livros
        self.inventario = []  # Lista para armazenar vários livros
    
    def adicionar_livro(self, livro):
        #adiciono o livro 
        self.inventario.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado ao inventário.")
    
    def emprestar_livro(self, titulo):
        #percorro na lista de livros se ele existe no meu acervo
        for livro in self.inventario:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"O livro '{titulo}' não foi encontrado no inventário.")
    
    def devolver_livro(self, titulo):
        for livro in self.inventario:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f"O livro '{titulo}' não foi encontrado no inventário.")
    
    def mostrar_inventario(self):
        if self.inventario:
            print("Inventário de Livros:")
            for livro in self.inventario:
                livro.mostrar_info()
        else:
            print("O inventário está vazio.")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("1984", "George Orwell")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

livraria.mostrar_inventario()

livraria.emprestar_livro("1984")
livraria.mostrar_inventario()

livraria.devolver_livro("1984")
livraria.mostrar_inventario()
