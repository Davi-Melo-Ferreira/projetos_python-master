import os

lista = [
    {1: {'nome': 'Camiseta', 'quantidade': 50, 'preco_unitario': 29.90}},
    {2: {'nome': 'Calça Jeans', 'quantidade': 20, 'preco_unitario': 99.90}},
    {3: {'nome': 'Tênis Esportivo', 'quantidade': 15, 'preco_unitario': 199.90}},
    {4: {'nome': 'Jaqueta', 'quantidade': 10, 'preco_unitario': 149.90}},
    {5: {'nome': 'Boné', 'quantidade': 30, 'preco_unitario': 39.90}},
]

while True:
    os.system('cls')

    print('Menu de Opções:'
          '\n1. Modificar um produto.'
          '\n2. Adicionar um produto.'
          '\n3. Remover um produto.'
          '\n4. Mostrar o estoque.')
    opcao = input('\nDigite uma das opções (1, 2, 3, 4): ')
    if opcao == '1':
        escolha0 = int(input('De qual número você deseja modificar?: '))
        escolha1 = escolha0 - 1
        escolha2 = str(input('O que você deseja modificar?'
                              '(nome, quantidade, preco_unitario): ')).lower()
        chave_principal = list(lista[escolha1].keys())[0]
        novo_valor = input(f"Digite o novo valor para '{escolha2}': ")
        if escolha2 in ['quantidade', 'preco_unitario']:
            novo_valor = float(novo_valor) if escolha2 == 'preco_unitario' else int(novo_valor)
        lista[escolha1][chave_principal][escolha2] = novo_valor

    elif opcao == '2':
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade em estoque: '))
        preco_unitario = float(input('Digite o preço unitário: '))
        novo_id = len(lista) + 1
        lista.append({novo_id: {'nome': nome, 'quantidade': quantidade, 'preco_unitario': preco_unitario}})
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '3':
        escolha_3 = int(input('De qual número você deseja remover?: '))
        ind_escolha = escolha_3 - 1
        if 0 <= ind_escolha < len(lista):
            del lista[ind_escolha]
            # Atualizar IDs
            for i, dicionario in enumerate(lista):
                chave_antiga = list(dicionario.keys())[0]
                dic_novo = {i + 1: dicionario[chave_antiga]}
                lista[i] = dic_novo
            print(f'Produto {escolha_3} removido com sucesso!')
        else:
            print('Número inválido! Nenhum produto foi removido.')
        input('\nPressione qualquer tecla para continuar...')

    elif opcao == '4':
        produtos_ordenados = sorted(lista, key=lambda x: x[list(x.keys())[0]]['nome'])
        print("\nEstoque de Produtos (Ordenado por Nome):")
        valor_total_estoque = 0
        for produto in produtos_ordenados:
            for id_produto, dados in produto.items():
                valor_total_estoque += dados['quantidade'] * dados['preco_unitario']
                print(f'ID: {id_produto}, Nome: {dados["nome"]}, Quantidade: {dados["quantidade"]}, '
                      f'Preço Unitário: R$ {dados["preco_unitario"]:.2f}')
        input(f'\nValor total do estoque: R$ {valor_total_estoque:.2f}\nPressione qualquer tecla para continuar...')
