from vendas import Venda, HistoricoVendas
from rh import Funcionario, SistemaRH
from conta import Conta

def main_menu():
    historico_vendas = HistoricoVendas()
    sistema_rh = SistemaRH()
    conta = Conta()

    while True:
        print("\nMenu:")
        print("1. Adicionar Venda")
        print("2. Total por Produto")
        print("3. Listar Vendas Acima de")
        print("4. Adicionar Funcionário")
        print("5. Aumentar Salário")
        print("6. Adicionar Transação")
        print("7. Filtrar Transações")
        print("8. Sair")

        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            nome_produto = input("Nome do Produto: ")
            quantidade = int(input("Quantidade: "))
            preco_unitario = float(input("Preço Unitário: "))
            venda = Venda(nome_produto, quantidade, preco_unitario)
            historico_vendas.adicionar_venda(venda)
        
        elif choice == '2':
            total = historico_vendas.total_por_produto()
            print("Total por Produto:", total)

        elif choice == '3':
            valor = float(input("Valor: "))
            vendas_acima = list(historico_vendas.listar_vendas_acima_de(valor))
            for venda in vendas_acima:
                print(f"Venda: {venda.nome_produto}, Total: {venda.total_venda():.2f}")

        elif choice == '4':
            nome = input("Nome do Funcionário: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            funcionario = Funcionario(nome, cargo, salario)
            sistema_rh.adicionar_funcionario(funcionario)

        elif choice == '5':
            nome = input("Nome do Funcionário para aumento: ")
            percentual = float(input("Percentual de aumento: "))
            for func in sistema_rh.funcionarios:
                if func.nome == nome:
                    sistema_rh.aumentar_salario(func, percentual)
                    break
            else:
                print("Funcionário não encontrado.")

        elif choice == '6':
            tipo = input("Tipo de transação (Depósito/Saque): ")
            valor = float(input("Valor: "))
            conta.adicionar_transacao({'tipo': tipo, 'valor': valor})

        elif choice == '7':
            tipo = input("Tipo de transação para filtrar: ")
            transacoes = conta.filtrar_transacoes_por_tipo(tipo)
            print("Transações filtradas:", transacoes)

        elif choice == '8':
            break

if __name__ == "__main__":
    main_menu()
