class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda t: t['tipo'] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(map(lambda t: {**t, 'valor': t['valor'] * (1 - taxa)} if t['tipo'] == 'Saque' else t, self.transacoes))
