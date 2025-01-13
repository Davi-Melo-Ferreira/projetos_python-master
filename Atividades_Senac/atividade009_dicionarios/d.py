import os

lista = [
    {1:
        {'nome': 'Vinho do Porto', 'tipo': 'Tinto',
        'teor_alcoolico': 20, 'safra': 2018}},
    {2:
        {'nome': 'Chardonnay', 'tipo': 'Branco',
        'teor_alcoolico': 13, 'safra': 2020}},
    {3:
        {'nome': 'Rosé Provence', 'tipo': 'Rosé',
        'teor_alcoolico': 12.5, 'safra': 2021}},
    {4:
        {'nome': 'Cabernet Sauvignon', 'tipo': 'Tinto',
        'teor_alcoolico': 14, 'safra': 2019}},
    {5:
        {'nome': 'Espumante Brut', 'tipo': 'Espumante',
        'teor_alcoolico': 11.5, 'safra': 2022}},
]

while True:
    os.system('cls')
    
    print('Menu de Opções:'
        '\n1. Modificar um Vinho.'
        '\n2. Adicionar um Vinho.'
        '\n3. Remover um Vinho.'
        '\n4. Mostrar o dicionário de Vinhos.')
        
    opcao = input('\nDigite uma das opções(1, 2, 3, 4): ')
    if opcao == '1':
        escolha0 = int(input('De qual número você deseja modificar?: '))
        escolha1 = escolha0 - 1  # Índice correspondente na lista
        escolha2 = str(input('O que você deseja modificar?'
                              ' (nome, tipo, teor_alcoolico, safra): ')).lower()
        chave_principal = list(lista[escolha1].keys())[0]
        novo_valor = input(f"Digite o novo valor para '{escolha2}': ")
        
        # Converte para número caso necessário
        if escolha2 in ['teor_alcoolico', 'safra']:
            novo_valor = float(novo_valor) if '.' in novo_valor else int(novo_valor)
        
        lista[escolha1][chave_principal][escolha2] = novo_valor

        print("\nDicionário atualizado!")
        input('\nPressione qualquer tecla para continuar...')

    # Adicionar um vinho
    elif opcao == '2':
        nome = input('Digite o nome do Vinho: ')
        tipo = input('Digite o tipo do vinho (Tinto, Branco, Rosé, etc.): ')
        teor = float(input('Digite o teor alcoólico (ex: 11.5): '))
        safra = int(input('Digite o ano da safra (ex: 2022): '))
        novo_id = len(lista) + 1
        lista.append({novo_id: {'nome': nome, 'tipo': tipo, 'teor_alcoolico': teor, 'safra': safra}})
        
        print("\nVinho adicionado com sucesso!")
        input('\nPressione qualquer tecla para continuar...')

    # Remover um vinho
    elif opcao == '3':
        escolha_3 = int(input('De qual número você deseja remover?: '))
        ind_escolha = escolha_3 - 1
        
        # Verifica se o número é válido
        if 0 <= ind_escolha < len(lista):
            del lista[ind_escolha]

            # Reorganiza os números dos vinhos
            for i, dicionario in enumerate(lista):
                chave_antiga = list(dicionario.keys())[0]
                dic_novo = {i + 1: dicionario[chave_antiga]}
                lista[i] = dic_novo
            
            print(f'Vinho {escolha_3} removido com sucesso!')
        else:
            print('Número inválido! Nenhum vinho foi removido.')
        input('\nPressione qualquer tecla para continuar...')

    # Mostrar o dicionário
    elif opcao == '4':
        print("\nDicionário de Vinhos:")
        for dicionario in lista:
            for id_lista, elementos in dicionario.items():
                print(f'\nVinho: {id_lista}')
                for key, value in elementos.items():
                    print(f'{key}: {value}')
        input('\nPressione qualquer tecla para continuar...')

    else:
        print("\nOpção inválida! Tente novamente.")
        input('\nPressione qualquer tecla para continuar...')