import os

meu_dicionario = {}
while True:
    os.system('cls')

    print('Menu de opções:'
        '\n1. Adicionar um dicionário.'
        '\n2. Remover um dicionário.'
        '\n3. Mostrar o dicionário.')
    
    opcao = input('\nQual opção você quer? (1-3): ')

    if opcao == '1':
        chave = input('Digite a chave: ')
        valor = input('Digite  o valor: ')
        dicionario = meu_dicionario.setdefault(chave, valor)
        input('\nConcluído... Pressione ENTER para continuar.')

    elif opcao == '2':
        procura = input('Digite a chave do dicionário que deseja remover: ')
        if procura in meu_dicionario:
            del meu_dicionario[procura]
            input('\nConcluído... Pressione ENTER para continuar.')
        else:
            input('O dicionário citado foi escrito errado ou não existe, Pressione ENTER')

    elif opcao == '3':
        print(meu_dicionario)
        input('\nConcluído... Pressione ENTER para continuar.')
    else:
        input('Valor Inválido! Por favor, pressione ENTER para reiniciar')