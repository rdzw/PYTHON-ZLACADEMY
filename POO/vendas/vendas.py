from functools import reduce

class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def total_venda(self):
        return self.quantidade * self.preco_unitario

class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        total_por_produto = {}
        for venda in self.vendas:
            if venda.nome_produto in total_por_produto:
                total_por_produto[venda.nome_produto] += venda.total_venda()
            else:
                total_por_produto[venda.nome_produto] = venda.total_venda()
        return total_por_produto

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.total_venda() > valor:
                yield venda
