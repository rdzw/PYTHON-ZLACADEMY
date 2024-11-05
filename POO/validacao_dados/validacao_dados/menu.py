# menu.py

from usuario import Usuario

class Menu:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        try:
            idade = int(input("Digite a idade do usuário: "))
        except ValueError:
            print("Idade inválida! Deve ser um número inteiro.")
            return
        
        email = input("Digite o email do usuário: ")

        try:
            novo_usuario = Usuario(nome, idade, email)
            self.usuarios.append(novo_usuario)
            print(f"Usuário {novo_usuario.nome} criado com sucesso!")
        except (ValueError, TypeError) as e:
            print(f"Erro ao criar usuário: {e}")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                print(usuario)

    def menu_principal(self):
        while True:
            print("\n----- MENU -----")
            print("1. Criar Usuário")
            print("2. Listar Usuários")
            print("3. Sair")
            opcao = int(input("Escolha uma opção: "))

            match opcao:
                case 1:
                    self.criar_usuario()
                case 2:
                    self.listar_usuarios()
                case 3:
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida!")
