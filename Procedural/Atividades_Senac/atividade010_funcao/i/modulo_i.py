import random

# Função para exibir os resultados
def exibir_reultado(acertos, qntd_perguntas):
    print('-'*70)
    print(f'Você acertou a capital de {acertos} estados(s).')
    print('-'*70)
    print(f'Resultado: {acertos}/{qntd_perguntas}\n')
    return acertos, qntd_perguntas


def randomizar(dicionario): # função para randomizar a ordem dos estados
        itens = list(dicionario.items()) # retorna uma tupla
        random.shuffle(itens) # embaralha os valores dentro da tupla
        estado_capital = dict(itens) # transforma a tupla em dicionário
        return estado_capital # packing
