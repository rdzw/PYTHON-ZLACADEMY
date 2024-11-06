import json
import csv
import pickle
from functools import reduce

# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano_publicacao}, genero='{self.genero}')"

# Classe que gerencia a biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))

    def exportar_para_texto(self, arquivo):
        with open(arquivo, 'w') as file:
            for livro in self.livros:
                file.write(f"{livro.titulo},{livro.autor},{livro.ano_publicacao},{livro.genero}\n")

    def importar_de_texto(self, arquivo):
        with open(arquivo, 'r') as file:
            for line in file:
                titulo, autor, ano, genero = line.strip().split(',')
                self.adicionar_livro(Livro(titulo, autor, int(ano), genero))

    def exportar_para_json(self, arquivo):
        with open(arquivo, 'w') as file:
            json.dump([livro.__dict__ for livro in self.livros], file)

    def importar_de_json(self, arquivo):
        with open(arquivo, 'r') as file:
            livros = json.load(file)
            for livro_data in livros:
                self.adicionar_livro(Livro(**livro_data))

    def exportar_para_csv(self, arquivo):
        with open(arquivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['titulo', 'autor', 'ano_publicacao', 'genero'])
            for livro in self.livros:
                writer.writerow([livro.titulo, livro.autor, livro.ano_publicacao, livro.genero])

    def importar_de_csv(self, arquivo):
        with open(arquivo, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.adicionar_livro(Livro(row['titulo'], row['autor'], int(row['ano_publicacao']), row['genero']))

    def exportar_para_binario(self, arquivo):
        with open(arquivo, 'wb') as file:
            pickle.dump(self.livros, file)

    def importar_de_binario(self, arquivo):
        with open(arquivo, 'rb') as file:
            self.livros = pickle.load(file)

    def listar_titulos(self):
        return list(map(lambda livro: livro.titulo, self.livros))

    def contar_livros_por_genero(self, genero):
        return reduce(lambda count, livro: count + 1 if livro.genero == genero else count, self.livros, 0)

    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: (ano is None or livro.ano_publicacao == ano) and 
                                          (genero is None or livro.genero == genero), self.livros))

    def backup(self, arquivo='backup.json', formato='json'):
        if formato == 'json':
            self.exportar_para_json(arquivo)
        elif formato == 'binario':
            self.exportar_para_binario(arquivo)

# Testes básicos do sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando livros
    biblioteca.adicionar_livro(Livro("1984", "George Orwell", 1949, "Distopia"))
    biblioteca.adicionar_livro(Livro("Orgulho e Preconceito", "Jane Austen", 1813, "Romance"))
    biblioteca.adicionar_livro(Livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967, "Realismo Mágico"))
    biblioteca.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"))
    biblioteca.adicionar_livro(Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Aventura"))

    # Consultando livros por autor
    livros_orwell = biblioteca.listar_livros_por_autor("George Orwell")
    print("Livros de George Orwell:", livros_orwell)

    # Contando livros por gênero
    total_fantasia = biblioteca.contar_livros_por_genero("Fantasia")
    print("Total de livros de fantasia:", total_fantasia)

    # Exportando e importando dados
    biblioteca.exportar_para_texto('biblioteca.txt')
    biblioteca.importar_de_texto('biblioteca.txt')

    biblioteca.exportar_para_json('biblioteca.json')
    biblioteca.importar_de_json('biblioteca.json')

    biblioteca.exportar_para_csv('biblioteca.csv')
    biblioteca.importar_de_csv('biblioteca.csv')

    biblioteca.exportar_para_binario('biblioteca.pkl')
    biblioteca.importar_de_binario('biblioteca.pkl')

    # Filtrando livros por ano e gênero
    livros_filtrados = biblioteca.filtrar_livros(ano=1949, genero="Distopia")
    print("Livros de 1949 do gênero Distopia:", livros_filtrados)

    # Realizando backup
    biblioteca.backup(arquivo='backup_biblioteca.json', formato='json')
    biblioteca.backup(arquivo='backup_biblioteca.pkl', formato='binario')
