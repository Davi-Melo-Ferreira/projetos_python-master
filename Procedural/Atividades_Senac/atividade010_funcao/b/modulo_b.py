
def cadastro(nome, matricula, nasc, dicionario):
    dicionario.update({'nome':nome, 'matricula':matricula, 'nascimento': nasc})
    return dicionario