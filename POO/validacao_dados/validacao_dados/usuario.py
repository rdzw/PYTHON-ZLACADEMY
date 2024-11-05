# usuario.py

class Usuario:
    def __init__(self, nome, idade, email):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        if not isinstance(idade, int):
            raise TypeError("A idade deve ser um número inteiro.")
        if "@" not in email:
            raise ValueError("O email deve conter '@'.")

        self.nome = nome
        self.idade = idade
        self.email = email
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"
