import os

produtos = {
    1: {'nome': 'Camiseta', 'preço': 29.90, 'categoria': 'Vestuário'},
    2: {'nome': 'Calça Jeans', 'preço': 99.90, 'categoria': 'Vestuário'},
    3: {'nome': 'Tênis Esportivo', 'preço': 199.90, 'categoria': 'Calçados'},
    4: {'nome': 'Jaqueta', 'preço': 149.90, 'categoria': 'Vestuário'},
    5: {'nome': 'Boné', 'preço': 39.90, 'categoria': 'Acessórios'},
}

def imprimir_lista(produtos):
    for id_produto, produto in produtos.items():
        print(f'{id_produto}: {produto["nome"]} - preço: R${produto["preço"]:.2f} - categoria: {produto["categoria"]}')

while True:
    os.system('cls')
    print('\nMenu de Opções:')
    print('1. Cadastrar novo produto')
    print('2. Alterar um produto')
    print('3. Aplicar descontos')
    print('4. Produtos ordenados por nome')
    print('5. Gerar relatório')

    opcao = input('\nEscolha uma opção (1, 2, 3, 4, 5): ')

    if opcao == '1':  # Cadastro de novo produto
        novo_id = len(produtos) + 1
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        categoria = input('Digite a categoria do produto: ')

        produtos[novo_id] = {
            'nome': nome,
            'preço': preco,
            'categoria': categoria
            }
        print('\nProduto cadastrado com sucesso!')
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '2':  # Alterar um produto
        if not produtos:
            print('\nNenhum produto cadastrado!')
        else:
            imprimir_lista(produtos)
            id_produto = int(input('\nDigite o ID do produto que deseja alterar: '))
            if id_produto in produtos:
                alterar = input('O que deseja alterar (nome, preço, categoria)?: ').lower()
                if alterar in produtos[id_produto]:
                    novo_valor = input(f'Digite o novo valor para {alterar}: ')
                    if alterar == 'preço':
                        novo_valor = float(novo_valor)
                    produtos[id_produto][alterar] = novo_valor
                    print('\nProduto alterado com sucesso!')
                else:
                    print('\nCampo inválido!')
            else:
                print('\nID de produto inválido!')
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '3':  # Aplicar descontos
        desconto = float(input('Digite o percentual de desconto (ex: 10 para 10%): '))
        print('\nDesconto aplicado com sucesso!')
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '4':  # Produtos ordenados por nome
        if not produtos:
            print('\nNenhum produto cadastrado!')
        else:
            produtos_ordenados = sorted(produtos.values(), key=lambda x: x['nome'])
            print('\nProdutos ordenados por nome:')
            def imprimir_lista_ordenada(produtos):
                for produto in produtos_ordenados:
                    print(f'{produto["nome"]} - preço: R${produto["preço"]:.2f} - categoria: {produto["categoria"]}')
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '5':  # Gerar relatório
        if not produtos:
            print('\nNenhum produto cadastrado!')
        else:
            imprimir_lista(produtos)
            for produto in produtos.values():
                abaixo_50 = 0
                eletronicos = 0
                if produto['preço'] * desconto / 100 < 50:
                       abaixo_50 += 1
                if produto['categoria'] == 'eletrônico':
                        eletronicos += 1
            print('\nRelatório:')
            print(f'Produtos com preço inferior a R$50: {abaixo_50}')
            print(f'Produtos na categoria "Eletrônicos": {eletronicos}')
        input('\nPressione qualquer tecla para continuar...')

    else:
        print('\nOpção inválida. Tente novamente.')
        input('\nPressione qualquer tecla para continuar...')