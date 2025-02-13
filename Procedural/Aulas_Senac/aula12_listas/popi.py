import os


os.system('cls')

lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90 ,100]

indice = int(input('Digite o índice do elemento a ser removido (0-9): '))

if 0 <= indice < len(lista_numeros):  
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('índice inválido!')
    
print('Lista após remoção:', lista_numeros)