import os


os.system('cls')

meu_dicionario = {}
while True:
    os.system('cls')

    print('Menu de opções:'
        '\n1. Adicionar uma cor.'
        '\n2. Remover uma cor.'
        '\n3. Mostrar o dicionário de cores.')
    
    opcao = input('\nQual opção você quer? (1-3): ')

    if opcao == '1':
        chave = input('Digite a cor: ')
        valor = input('Digite  a descrição: ')
        dicionario = meu_dicionario.setdefault(chave, valor)
        input('\nConcluído... Pressione ENTER para continuar.')

    elif opcao == '2':
        procura = input('Digite a cor que deseja remover: ')
        if procura in meu_dicionario:
            del meu_dicionario[procura]
            input('\nConcluído... Pressione ENTER para continuar.')
        else:
            input('A cor citada foi escrito errado ou não existe, Pressione ENTER')

    elif opcao == '3':
        print(meu_dicionario)
        
        sortudo = sorted(meu_dicionario)
        print('Chaves em ordem alfabética:', sortudo)

        dicionario = list(meu_dicionario.copy())

        alph = 'abcdefghijklmnopqrstuvwxyz'

        for char in alph:
                num = 0
                for elemento in dicionario:
                    if char in elemento[0]:
                        num += 1
                if num == 0:
                    continue
                else:
                    print(f'Existe(m) {num} cor(es) que começa(m) com a letra: {char}')
                
                input('\nConcluído... Pressione ENTER para continuar.')
    else:
        input('Valor Inválido! Por favor, pressione ENTER para reiniciar')