from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print("Pagamento com cartão de crédito processado.")

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto):
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print("Pagamento com boleto processado.")

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print("Pagamento via Pix processado.")

def processar(pagamento: Pagamento):
    pagamento.processar_pagamento()

# Exemplo de uso
cartao = PagamentoCartaoCredito("1234-5678-9876-5432")
boleto = PagamentoBoleto("000111222333")
pix = PagamentoPix("chavepix123")

processar(cartao)
processar(boleto)  
processar(pix)     
