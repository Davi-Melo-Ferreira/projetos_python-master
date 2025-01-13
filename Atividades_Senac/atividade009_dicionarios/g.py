# f
import os

# Lista de pessoas
lista = [
    {1: {'nome': 'João', 'idade': 25, 'peso': 70.5, 'altura': 1.75}},
    {2: {'nome': 'Maria', 'idade': 30, 'peso': 60.2, 'altura': 1.68}},
    {3: {'nome': 'Carlos', 'idade': 28, 'peso': 80.3, 'altura': 1.80}},
    {4: {'nome': 'Ana', 'idade': 22, 'peso': 55.0, 'altura': 1.65}},
    {5: {'nome': 'Pedro', 'idade': 35, 'peso': 90.7, 'altura': 1.85}}
]

# o def serve pra resumir linhas em um nome 
def exibir_dados(lista):
    #Printando o dicionário
    for dicionario in lista:
        for id_lista, elementos in dicionario.items():
            print(f'\nDicionário: {id_lista}')
            for key, value in elementos.items():
                print(f'{key}: {value}')
    
def exibir_nome_altura(lista):
#Exibindo apenas nome e altura
    for dicionario in lista:
        for id_lista, elementos in dicionario.items():
            print(f'{id_lista} - Nome: {elementos["nome"]} - Altura: {elementos["altura"]}')

def menu():
    os.system('cls')
    print('Menu de Opções:')
    print('1. Listar todas as chaves e valores do dicionário.')
    print('2. Alterar o valor de uma chave.')
    print('3. Excluir um item específico.')
    print('4. Exibir apenas o nome e a altura.')
    print('5. Gerar relatório final.')

while True:
    menu()
    opcao = input('\nDigite uma das opções (1, 2, 3, 4, 5): ')

    # Listar todas as chaves e valores
    if opcao == '1':
        exibir_dados(lista)
        input('\nPressione qualquer tecla para continuar...')

    # Alterar o valor de uma chave
    elif opcao == '2':
        id_alterar = int(input('Digite o ID do item que deseja alterar: '))
        chave_alterar = input('Digite o nome da chave que deseja alterar (nome, idade, peso, altura): ').lower()
        novo_valor = input(f'Digite o novo valor para a chave {chave_alterar}: ')
        
        encontrado = False
        for dicionario in lista:
            if id_alterar in dicionario:
                if chave_alterar in dicionario[id_alterar]:
                    dicionario[id_alterar][chave_alterar] = novo_valor
                    encontrado = True
                    print(f'Chave {chave_alterar} atualizada para: {novo_valor}')
                else:
                    print(f'A chave "{chave_alterar}" não existe nesse item.')
        
        if not encontrado:
            print(f'O item com ID {id_alterar} não foi encontrado.')

        input('\nPressione qualquer tecla para continuar...')

    # Excluir um item específico
    elif opcao == '3':
        id_excluir = int(input('Digite o ID do item que deseja excluir: '))
        
        encontrado = False
        for i, dicionario in enumerate(lista):
            if id_excluir in dicionario:
                del lista[i]
                encontrado = True
                print(f'O item com ID {id_excluir} foi excluído com sucesso.')
                break
        
        if not encontrado:
            print(f'O item com ID {id_excluir} não foi encontrado.')

        input('\nPressione qualquer tecla para continuar...')

    # Exibir apenas o nome e a altura
    elif opcao == '4':
        print("\nExibindo apenas nome e altura:")
        exibir_nome_altura(lista)
        input('\nPressione qualquer tecla para continuar...')

    # Gerar relatório final
    elif opcao == '5':
        print("\nGerando relatório final...")

        total_dados = 0
        for dicionario in lista:
            for id_lista, elementos in dicionario.items():
                total_dados += 1
        
        print(f'Número total de itens no dicionário: {total_dados}')
        print('Estado atual das chaves e valores:')
        exibir_dados(lista)
        
        input('\nPressione qualquer tecla para continuar...')