def dado(lados):
    from random import randint
    return randint(1, lados)


def rolar(quantidade_Dado, lados_Dado):
    soma_valor = 0
    for contador in range(0, quantidade_Dado):
        soma_valor += dado(lados_Dado)
    return soma_valor
