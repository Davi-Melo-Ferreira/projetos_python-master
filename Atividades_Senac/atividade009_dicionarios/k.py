import os
from datetime import datetime, timedelta

tarefas = {}

while True:
    os.system('cls')
    print('\nMenu de Opções:')
    print('1. Cadastrar nova tarefa')
    print('2. Alterar prioridade ou data de vencimento de uma tarefa')
    print('3. Listar tarefas ordenadas por data de vencimento')
    print('4. Gerar relatório')

    opcao = input('\nEscolha uma opção (1, 2, 3, 4): ')

    if opcao == '1':  # Cadastro de nova tarefa
        novo_id = len(tarefas) + 1
        nome_tarefa = input('Digite o nome da tarefa: ')

        # Validação de data usando um loop
        while True:
            data_vencimento = input('Digite a data de vencimento (dd/mm/aaaa): ')
            try:
                data_verify = datetime.strptime(data_vencimento, '%d/%m/%Y')  # Tenta converter a data
                break  # Sai do loop se a data for válida
            except ValueError:
                print('Data inválida! Certifique-se de usar o formato correto e valores válidos.')

        prioridade = input('Digite a prioridade (alta, média, baixa): ').lower()

        # Verifica se a prioridade é válida
        while prioridade not in ['alta', 'média', 'baixa']:
            prioridade = input('Prioridade inválida! Escolha entre alta, média ou baixa: ').lower()

        # Cadastra a tarefa
        tarefas[novo_id] = {
            'nome': nome_tarefa,
            'data_vencimento': data_vencimento,
            'prioridade': prioridade,
        }

        print('\nTarefa cadastrada com sucesso!')
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '2': # Alterar prioridade ou data de vencimento de uma tarefa
        if not tarefas:
            print('\nNenhuma tarefa cadastrada! Cadastre uma tarefa antes de alterar.')
            input('\nPressione qualquer tecla para continuar...')
            continue
        print('\nTarefas disponíveis:')
        for id_tarefa, tarefa in tarefas.items():
            print(f'{id_tarefa}: {tarefa["nome"]} - Vencimento: {tarefa["data_vencimento"]} - Prioridade: {tarefa["prioridade"]}')

        id_tarefa = int(input('\nDigite o ID da tarefa que deseja alterar: '))

        if id_tarefa in tarefas:
                print('\nO que você deseja alterar?')
                print('1. Prioridade')
                print('2. Data de vencimento')
                escolha = input('\nEscolha uma opção (1, 2): ')

                if escolha == '1':
                    nova_prioridade = input('Digite a nova prioridade (alta, média, baixa): ').lower()
                    if nova_prioridade not in ['alta', 'média', 'baixa']:
                        nova_prioridade = input('Prioridade inválida! Escolha entre alta, média ou baixa: ').lower()
                    else:
                        tarefas[id_tarefa]['prioridade'] = nova_prioridade
                        print('\nPrioridade alterada com sucesso!')
                elif escolha == '2':
                    nova_data = input('Digite a nova data de vencimento (dd/mm/aaaa): ')
                    tarefas[id_tarefa]['data_vencimento'] = nova_data
                    print('\nData de vencimento alterada com sucesso!')
                else:
                    ('\nOpção inválida!')
        else:
            print('\nID de tarefa inválido!')

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '3': # Tarefas ordenadas por data de vencimento
        if not tarefas:
            print('\nNenhuma tarefa cadastrada!')
        else:
            print('\nLista de Tarefas Ordenadas por Data de Vencimento:')
            # x = {'nome': 'Revisar projeto', 'data_vencimento'...... 
            tarefas_ordenadas = sorted(tarefas.values(), key=lambda x: datetime.strptime(x['data_vencimento'], '%d/%m/%Y'))
            for tarefa in tarefas_ordenadas:
                print(f'Tarefa: {tarefa["nome"]} - Vencimento: {tarefa["data_vencimento"]} - Prioridade: {tarefa["prioridade"]}')

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '4':
        # Gerar relatório
        if not tarefas:
            print('\nNenhuma tarefa cadastrada!')
        else:
            hoje = datetime.today() # define a data de hoje
            proximo_mes = hoje + timedelta(days=30) # timedelta define uma data
            tarefas_prioridade_alta = 0
            tarefas_proximo_mes = 0

            for tarefa in tarefas.values():
                data_venc = datetime.strptime(tarefa['data_vencimento'], '%d/%m/%Y')
                if tarefa['prioridade'] == 'alta':
                    tarefas_prioridade_alta += 1
                # verifica se a data de vencimento está próximo de um mês
                if hoje <= data_venc <= proximo_mes:
                    tarefas_proximo_mes += 1

            print('\nRelatório:')
            print(f'Total de tarefas cadastradas: {len(tarefas)}')
            print(f'Tarefas com prioridade alta: {tarefas_prioridade_alta}')
            print(f'Tarefas com vencimento no próximo mês: {tarefas_proximo_mes}')

        input('\nPressione qualquer tecla para continuar...')
    else:
        print('\nOpção inválida. Tente novamente.')