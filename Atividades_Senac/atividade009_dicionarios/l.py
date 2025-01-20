#listar os filmes ordenados por título, e gerar um relatório que indique quantos filmes têm duração superior a 2 horas e quantos tem classificação indicativa 'Livre'.
import os

def imprimir_lista(filmes):
    print('\nLista de Filmes:')
    for id_filme, filme in filmes.items():
        print(f'\nFilme {id_filme}. \nTítulo: {filme["título"]} - Gênero: {filme["gênero"]} - Duração: {filme["duração"]} - Classificação: {filme["classificação"]}')

filmes = {}
while True:
    os.system('cls')
    print('\nMenu de Opções:')
    print('1. Cadastrar um novo filme')
    print('2. Alterar um filme')
    print('3. Remover um filme')
    print('4. Gerar relatório')

    opcao = input('\nEscolha uma opção (1, 2, 3, 4): ')

    if opcao == '1': # Cadastrar filme
        id_novo = len(filmes) + 1
        titulo = input('Digite o Título do filme: ')
        genero = input('Digite o gênero do filme(terror, ação...): ')
        duracao = input('Digite a duração do filme(02:30:00): ')
        classificacao = input('Digite a classificação do filme(livre, 10, 12, 12, 16 e 18): ').lower()
        
        filmes[id_novo] = {
            'título':titulo,
            'gênero':genero,
            'duração':duracao,
            'classificação':classificacao
        }
        
        print('\nFilme adicionado com sucesso')
        input('Pressione qualquer tecla para continuar....')

    if opcao == '2': # Alterar filme
        if not filmes:
            print('\nNenhum filme cadastrado!')
        else:
            imprimir_lista(filmes)
            opcao_id = input('Digite o id do filme que deseja editar: ')
            opcao_valor = input(f'O que você deseja alterar do filme {opcao_id}?: ')
            novo_valor = input(f'Digite o novo valor para {opcao_valor}: ')
            filmes[opcao_id][opcao_valor] = novo_valor
            print('\nFilme alterado com sucesso')
        input('Pressione qualquer tecla para continuar....')
        
    if opcao == '3': # Deletar filme
        if not filmes:
            print('\nNenhum filme cadastrado!')
        else:
            imprimir_lista(filmes)
            opcao_id = input('Digite o id do filme que deseja deletar: ')
            if filmes[opcao_id]:
                del filmes[opcao_id]
                input('\n Concluído!!! Pressione qualquer tecla para continuar....')
                
    if opcao == '4': # x = {'nome': 'Revisar projeto', 'data_vencimento'...... 
        filmes_ordenados = sorted(filmes.values(), key=lambda x: (x['título'])) #lambda é quase como se fosse um for x: pegue de x o título
        id_filmes = 0
        cont_duracao = 0
        cont_classif = 0
        for filmes in filmes_ordenados:
            id_filmes += 1
            if filmes['classificação'] == 'livre':
                cont_classif += 1
            if int(filmes['duração'][1]) > 2:
                cont_duracao += 1
            
            print('\nFilmes ordenados por título')
            print(f'\nFilme {id_filmes}. \nTítulo: {filmes["título"]} - Gênero: {filmes["gênero"]} - Duração: {filmes["duração"]} - Classificação: {filmes["classificação"]}')
            print(f'\n Existem {cont_classif} filmes que possuem indicação livre')
            print(f'\n Existem {cont_duracao} filmes que tem uma duração maior de 2 horas')
            input('\nPressione qualquer tecla para continuar....')
    else:
        print('Nenhum Filme Cadastrado')
        input('\nPressione qualquer tecla para continuar....')