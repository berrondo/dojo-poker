
combinacoes = {
           # mesmo naipe, sequencia de 5
    ((1, 1, 1, 1, 1), (0, 0)): 0,  # CartaAlta,
    ((1, 1, 1, 1, 1), (0, 1)): 4,  # Straight,
    ((1, 1, 1, 1, 1), (1, 0)): 5,  # Flush,
    ((1, 1, 1, 1, 1), (1, 1)): 8,  # StraightFlush,
                             # 9,  # RoyalFlush, ou StraightFlush com As
    
    ((1, 1, 1, 2),    (0, 0)): 1,  # Par,
    ((1, 1, 1, 2),    (1, 0)): 5,  # Flush,
    
    ((1, 2, 2),       (0, 0)): 2,  # DoisPares,
    ((1, 2, 2),       (1, 0)): 5,  # Flush,
    
    ((1, 1, 3),       (0, 0)): 3,  # Trinca,
    ((1, 1, 3),       (1, 0)): 5,  # Flush,
    
    ((2, 3),          (0, 0)): 6,  # FullHouse,
    ((2, 3),          (1, 0)): 6,  # FullHouse, mesmo naipe
    
    ((1, 4),          (0, 0)): 7,  # Quadra,
    ((1, 4),          (1, 0)): 7,  # Quadra, mesmo naipe
}


def combinacao(mao):
    valores = map('0123456789DJQKA'.index, mao[::3])

    eh_mesmo_naipe = int(len(set(mao[1::3])) == 1) or 0
    eh_sequencia = int(max(valores) - min(valores) == 4) or 0
    
    quantos_de_cada = {}
    for valor in valores:
        quantos_de_cada[valor] = quantos_de_cada.get(valor, 0) + 1
        
    mais_combinados = max(quantos_de_cada.values())
    menos_combinados = min(quantos_de_cada.values())
        
    maior_valor_combinado = 0
    maior_valor_restante = 0
    for valor, quantidade in quantos_de_cada.items():
        if quantidade == mais_combinados:
            maior_valor_combinado = max(maior_valor_combinado, valor)
        if quantidade == menos_combinados:
            maior_valor_restante = max(maior_valor_restante, valor)

    return (
        combinacoes[tuple(sorted(quantos_de_cada.values())), (eh_mesmo_naipe, eh_sequencia)], 
        maior_valor_combinado, 
        maior_valor_restante,
    )


def poker(mao1, mao2):
    if combinacao(mao1) == combinacao(mao2):
        print combinacao(mao1), combinacao(mao2)
        raise ValueError
        
    if combinacao(mao1) > combinacao(mao2):
        return 1
    return 2