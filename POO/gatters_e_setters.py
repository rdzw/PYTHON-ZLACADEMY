class Livro:
    def _init_(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True  # Por padrão, o livro é disponível
    
    # Getter para título
    @property
    def titulo(self):
        return self._titulo
    
    # Setter para título (caso queira permitir a alteração, mas não é comum alterar título)
    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    # Getter para autor
    @property
    def autor(self):
        return self._autor
    
    # Getter para disponibilidade
    @property
    def disponivel(self):
        return self._disponivel

    # Setter para disponibilidade
    @disponivel.setter
    def disponivel(self, status):
        self._disponivel = status
    
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
    def _init_(self):
        # Lista para armazenar vários livros
        self.inventario = []
    
    def adicionar_livro(self, livro):
        self.inventario.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado ao inventário.")
    
    def emprestar_livro(self, titulo):
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

# Testando a implementação
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