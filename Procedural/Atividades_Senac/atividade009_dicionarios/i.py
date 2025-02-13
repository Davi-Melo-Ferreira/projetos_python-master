import os

produtos = {
    1: {'nome': 'Camiseta', 'quantidade': 50, 'preço unitário': 29.90},
    2: {'nome': 'Calça Jeans', 'quantidade': 20, 'preço unitário': 99.90},
    3: {'nome': 'Tênis Esportivo', 'quantidade': 15, 'preço unitário': 199.90},
    4: {'nome': 'Jaqueta', 'quantidade': 10, 'preço unitário': 149.90},
    5: {'nome': 'Boné', 'quantidade': 30, 'preço unitário': 39.90},
}


def imprimir_lista(produtos):
    for id_tarefa, produto in produtos.items():
        print(f'{id_tarefa}: {produto["nome"]} - quantidade: {produto["quantidade"]} - preço unitário: {produto["preço unitário"]}')


while True:
    os.system('cls')
    print('\nMenu de Opções:')
    print('1. Cadastrar novo produto')
    print('2. Alterar um produto')
    print('3. produtos ordenadas por data de vencimento')
    print('4. Gerar relatório')

    opcao = input('\nEscolha uma opção (1, 2, 3, 4): ')

    if opcao == '1':  # Cadastro de novo produto
        novo_id = len(produtos) + 1
        nome = input('Digite o nome da produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o preço unitário do produto: '))

        # Cadastra a produto
        produtos[novo_id] = {
            'nome': nome,
            'quantidade': quantidade,
            'preço': preco,
        }

        print('\nProduto cadastrado com sucesso!')
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '2':  # Alterar um produto
        if not produtos:
            print('\nNenhuma produto cadastrado! Cadastre um produto antes de alterar.')
            input('\nPressione qualquer tecla para continuar...')
            continue
        print('\nprodutos disponíveis:')
        imprimir_lista(produtos)
        id_tarefa = int(input('\nDigite o ID da produto que deseja alterar: '))

        if id_tarefa in produtos:
            escolha = input('\nO que você deseja alterar?: ')
            if escolha not in produtos[id_tarefa]:
                print('Inválido!')
            else:
                novo_valor = input(
                    'Digite o novo valor que queira adicionar: ')
                produtos[id_tarefa][escolha] = novo_valor
                print('\nPrioridade alterada com sucesso!')
        else:
            print('\nID de produto inválido!')

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '3':  # produtos ordenadas por nome
        if not produtos:
            print('\nNenhuma produto cadastrado!')
        else:
            print('\nprodutos de produtos Ordenadas por Nome:')
            # x = {'nome': 'Revisar projeto', 'quantidade'......
            produtos_ordenadas = sorted(
                produtos.values(), key=lambda x: (x['nome']))
            for produto in produtos_ordenadas:
                print(f'Tarefa: {produto["nome"]} - quantidade: {produto["quantidade"]} - preço unitário: {produto["preço unitário"]}')

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '4':
        # Gerar relatório
        if not produtos:
            print('\nNenhuma produto cadastrado!')
        else:
            total = 0
            for id_tarefa, produto in produtos.items():
                total += produto['quantidade'] * produto['preço unitário']
            imprimir_lista
            print('Valor total do estoque:', total)
        input('\nPressione qualquer tecla para continuar...')
    else:
        print('\nOpção inválida. Tente novamente.')
