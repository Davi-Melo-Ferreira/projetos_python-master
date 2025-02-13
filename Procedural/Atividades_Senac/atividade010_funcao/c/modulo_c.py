
# função para adicionar o cadastro
def cadastrar(id, nome, matricula, nascimento, cadastro):
    cadastro[id] = { # aqui diz: id chave foi atribuido o valor {'nome':nome.....}
        'nome':nome,
        'matricula':matricula,
        'nascimento':nascimento
    }
    return cadastro