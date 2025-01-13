import os

livros = {
    1: {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien',
        'ano': 1954, 'paginas': 1216},
    2: {'titulo': '1984', 'autor': 'George Orwell',
        'ano': 1949, 'paginas': 328},
    3: {'titulo': 'Harry Potter e a Pedra Filosofal','autor': 'J.K. Rowling',   'ano': 1997, 'paginas': 223}
}

while True:
    os.system('cls')
    print("\nMenu de Opções:")
    print("1. Adicionar um novo livro")
    print("2. Alterar dados de um livro")
    print("3. Listar todos os livros")
    print("4. Gerar relatório")

    opcao = input("\nEscolha uma opção (1, 2, 3, 4): ")

    if opcao == '1':
        novo_id = len(livros) + 1
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação: "))
        paginas = int(input("Digite o número de páginas: "))
        
        livros[novo_id] = {'titulo': titulo, 'autor': autor, 'ano': ano, 'paginas': paginas}
        print("\nNovo livro cadastrado com sucesso!")
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '2':
        id_livro = int(input("\nDigite o número do livro a ser alterado (ID): "))
        if id_livro in livros:
            livro = livros[id_livro]
            print("\nO que você deseja alterar?")
            print("1. Título")
            print("2. Autor")
            print("3. Ano de Publicação")
            print("4. Número de Páginas")
            escolha = int(input("Escolha uma opção (1, 2, 3, 4): "))
            
            if escolha == 1:
                novo_titulo = input("Digite o novo título: ")
                livro['titulo'] = novo_titulo
            if escolha == 2:
                novo_autor = input("Digite o novo autor: ")
                livro['autor'] = novo_autor
            if escolha == 3:
                novo_ano = int(input("Digite o novo ano de publicação: "))
                livro['ano'] = novo_ano
            if escolha == 4:
                novas_paginas = int(input("Digite o novo número de páginas: "))
                livro['paginas'] = novas_paginas
            
            print("\nLivro alterado com sucesso!")
        else:
            print("Livro não encontrado!")
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '3':
        livros_ordenados = sorted(livros.items(), key=lambda x: x[1]['titulo'])
        print("\nLista de Livros Cadastrados (Ordenados por Título):")
        for _, livro in livros_ordenados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Páginas: {livro['paginas']}")
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '4':
        total_livros = len(livros)
        livros_mais_300_paginas = 0
        livros_jk_rowling = 0
        
        for livro in livros.values():
            if livro['paginas'] > 300:
                livros_mais_300_paginas += 1
            if livro['autor'].lower() == 'j.k. rowling':
                livros_jk_rowling += 1
        
        print(f"\nRelatório:")
        print(f"Total de livros cadastrados: {total_livros}")
        print(f"Livros com mais de 300 páginas: {livros_mais_300_paginas}")
        print(f"Livros de J.K. Rowling: {livros_jk_rowling}")
        input('\nPressione qualquer tecla para continuar...')

    else:
        print("\nOpção inválida. Tente novamente.")