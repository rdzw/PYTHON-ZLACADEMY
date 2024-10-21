class calculadora:
    def adicionar(self, *args):
        return sum(args)
    
calc = calculadora
print(calc.adicionar(5))
print(calc.adicionar(5, 10))
print(calc.adicionar(5,10,15))