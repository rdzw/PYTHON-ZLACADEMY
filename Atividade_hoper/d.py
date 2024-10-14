def verificar_tempo_espera(fila_pedidos, tempo_maximo=15):
    """
    Verifica se algum pedido na fila ultrapassou o tempo máximo de espera.

    Parâmetros:
    fila_pedidos (dict): Dicionário de pedidos com ID e tempo de espera (em minutos).
    tempo_maximo (int): Tempo máximo de espera permitido (em minutos). Padrão é 15 minutos.

    Retorna:
    list: IDs dos pedidos que ultrapassaram o tempo máximo de espera.
    """
    pedidos_ultrapassaram = []

    for pedido_id, tempo_espera in fila_pedidos.items():
        if tempo_espera > tempo_maximo:
            pedidos_ultrapassaram.append(pedido_id)

    return pedidos_ultrapassaram

# Exemplo de uso
fila_pedidos = {
    'pedido_1': 10,
    'pedido_2': 20,
    'pedido_3': 5,
    'pedido_4': 25,
}

resultado = verificar_tempo_espera(fila_pedidos)
print(f"Pedidos que ultrapassaram o tempo máximo de espera: {resultado}")
