
def cadastrar(codigo, nome, altura, peso, dicionario):
        dicionario[codigo] = {'nome': nome, 'altura': altura, 'peso': peso}
        return dicionario
    
def gerar_somas(cadastrados):
    soma_peso = 0
    soma_altura = 0
    for dicionario in cadastrados.values():
        soma_peso += dicionario['peso']
        soma_altura += dicionario['altura']
    return soma_altura, soma_peso