
def verificar_paridade(lista):
    
    lista_par = []
    lista_impar = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return lista_par, lista_impar

def quantidades(lista_par, lista_impar):
    qntd_par = len(lista_par)
    qntd_impar = len(lista_impar)
    return qntd_par, qntd_impar
