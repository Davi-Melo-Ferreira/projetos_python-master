import os
from datetime import datetime

def imprimir_lista(viagens):
    print('\nLista de viagens:')
    for id_viagem, viagem in viagens.items():
        print(f'\nViagem {id_viagem}. \Destino: {viagem["destino"]} - data de partida: {viagem["data de partida"]} - Duração: {viagem["duração"]} - Vagas: {viagem["vagas"]}')

viagens = {
    1:{'destino':'albuquerque', 'data de partida': '06/05/2025', 'duração': '01:30:15', 'vagas': '2'},
    2:{'destino':'Xique xique', 'data de partida': '12/10/2025', 'duração': '02:30:00', 'vagas': '3'}
}

while True:
    os.system('cls')
    print('\nMenu de Opções:')
    print('1. Cadastrar uma nova viagem')
    print('2. Alterar uma viagem')
    print('3. Remover uma viagem')
    print('4. Gerar relatório')

    opcao = input('\nEscolha uma opção (1, 2, 3, 4): ')

    if opcao == '1':
        id_novo = len(viagens) + 1
        destino = input('Digite o destino da viagem: ')
        data_partida = input('Digite a data de partida da viagem(01/06/2025): ')
        duracao = input('Digite a duração do viagem(02:30:00): ')
        vagas = input('Digite a vagas do viagem(1, 2, 3...): ').lower()
        
        viagens[id_novo] = {
            'destino':destino,
            'data de partida':data_partida,
            'duração':duracao,
            'vagas':vagas
        }
        print('\nviagem adicionada com sucesso')
        input('Pressione qualquer tecla para continuar....')
    if opcao == '2':
        if not viagens:
            print('\nNenhuma viagem cadastrada!')
        else:
            imprimir_lista(viagens)
            opcao_id = input('Digite o id da viagem que deseja editar: ')
            opcao_valor = input(f'O que você deseja alterar da viagem {opcao_id}?: ')
            novo_valor = input(f'Digite o novo valor para {opcao_valor}: ')
            viagens[opcao_id][opcao_valor] = novo_valor
            print('\nviagem alterada com sucesso')
        input('Pressione qualquer tecla para continuar....')
    if opcao == '3':
        if not viagens:
            print('\nNenhuma viagem cadastrada!')
        else:
            imprimir_lista(viagens)
            opcao_id = input('Digite o id da viagem que deseja deletar: ')
            if viagens[opcao_id]:
                del viagens[opcao_id]
                input('\n Concluído!!! Pressione qualquer tecla para continuar....')
                
    if opcao == '4':
        # Ordenar viagens pelo destino
        viagems_ordenados = sorted(viagens.values(), key=lambda x: x['destino'])  # Ordena pelo destino
        cont_duracao = 0
        cont_classif = 0

        # Contar viagens com menos de 10 vagas e viagens após 01/06/2025
        for values in viagens.values():
            if int(values['vagas']) < 10:
                cont_classif += 1
            data_venc = datetime.strptime('01/06/2025', '%d/%m/%Y')
            data = datetime.strptime(values['data de partida'], '%d/%m/%Y')
            if data > data_venc:
                cont_duracao += 1

        # Exibir viagens ordenadas por destino
        print('\nViagens ordenadas por destino:')
        for ind, items in enumerate(viagems_ordenados, start=1):
            print(f'Viagem {ind}. Destino: {items["destino"]} - Data de partida: {items["data de partida"]} - '
                f'Duração: {items["duração"]} - Vagas: {items["vagas"]}')

        # Exibir contagens gerais fora do loop
        print(f'\nExistem {cont_classif} viagens que possuem menos de 10 vagas.')
        print(f'Existem {cont_duracao} viagens que ocorrem após o dia 01/06/2025.')
        input('\nPressione qualquer tecla para continuar....')