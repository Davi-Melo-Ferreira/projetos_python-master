import os


os.system('cls')

lista = [1, 2, 3, 4]

posicao = int(input('Posição onde deseja inserir o elemento'))
elemento = input('Elemento a ser inserido: ')

if posicao >= 0 and posicao <= len(lista):
    
    lista.insert(posicao, elemento)
    print('Lista após a inserção', lista)
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')