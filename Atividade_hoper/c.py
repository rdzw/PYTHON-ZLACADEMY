from datetime import datetime

def atualiza_tempo_entrega(fila_pedidos, id_pedido):
    """
    Atualiza o tempo de entrega de um pedido e calcula o tempo total de espera.

    Parâmetros:
    fila_pedidos (dict): O dicionário de pedidos.
    id_pedido (str): O identificador do pedido cujo tempo de entrega está sendo atualizado.

    Retorna:
    int: O tempo total de espera (em minutos) desde o momento em que o pedido foi feito até o momento em que foi entregue.
    """
    pedido = fila_pedidos[id_pedido]
    tempo_total_espera = (datetime.now() - pedido['tempo_criacao']).total_seconds() / 60
    return int(tempo_total_espera)

# Exemplo de uso
fila_pedidos = {
    '001': {'tempo_criacao': datetime(2024, 7, 31, 14, 30)},
    '002': {'tempo_criacao': datetime(2024, 7, 31, 15, 0)},
}

id_pedido = '001'
tempo_espera = atualiza_tempo_entrega(fila_pedidos, id_pedido)
print(f"Tempo total de espera para o pedido {id_pedido}: {tempo_espera} minutos")
