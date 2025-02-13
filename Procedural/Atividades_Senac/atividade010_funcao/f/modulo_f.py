
def receber_dicionario(lista_1, lista_2, dicionario):
    for chave, valor in zip(lista_1, lista_2):
        dicionario[chave] = valor
    return dicionario