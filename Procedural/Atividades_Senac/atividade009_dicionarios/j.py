import os
from datetime import datetime

# Dicionário para armazenar eventos e participantes
eventos = {}

while True:
    os.system('cls')
    print("\nMenu de Opções:")
    print("1. Cadastrar um novo evento")
    print("2. Associar participantes a um evento")
    print("3. Listar eventos com participantes")
    print("4. Gerar relatório")


    opcao = input("\nEscolha uma opção (1, 2, 3, 4): ")

    if opcao == '1':
        # Cadastro de um novo evento
        novo_id = len(eventos) + 1
        nome_evento = input("Digite o nome do evento: ")
        data_evento = input("Digite a data do evento (dd/mm/aaaa): ")
        local_evento = input("Digite a localização do evento: ")

        eventos[novo_id] = {
            'nome': nome_evento,
            'data': data_evento,
            'local': local_evento,
            'participantes': []
        }

        print("\nEvento cadastrado com sucesso!")
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '2':
        # Associar participantes a um evento
        if not eventos: # se eventos estiver vazio
            print("\nNenhum evento cadastrado! Cadastre um evento antes de adicionar participantes.")
            input('\nPressione qualquer tecla para continuar...')
            continue

        print("\nEventos disponíveis:")
        for id_evento, evento in eventos.items():
            print(f"{id_evento}. {evento['nome']} - Data: {evento['data']} - Local: {evento['local']}")

        id_evento = int(input("\nDigite o ID do evento que deseja adicionar participantes: "))

        if id_evento in eventos:
            while True:
                nome_participante = input("Digite o nome do participante: ")
                email_participante = input("Digite o email do participante: ")
                # adiciona nome e email com append
                eventos[id_evento]['participantes'].append({
                    'nome': nome_participante,
                    'email': email_participante
                })
                print("\nParticipante adicionado com sucesso!")

                continuar = input("Deseja adicionar outro participante a este evento? (s/n): ").lower()
                if continuar != 's':
                    break
        else:
            print("\nID de evento inválido!")

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '3':
        # Listar eventos com participantes
        if not eventos:
            print("\nNenhum evento cadastrado!")
        else:
            print("\nLista de eventos com participantes:")
            for id_evento, evento in eventos.items():
                print(f"\nEvento: {evento['nome']} - Data: {evento['data']} - Local: {evento['local']}")
                print("Participantes:")
                if evento['participantes']:
                    for participante in evento['participantes']:
                        print(f"  Nome: {participante['nome']}, Email: {participante['email']}")
                else:
                    print("  Nenhum participante associado.")

        input('\nPressione qualquer tecla para continuar...')

    if opcao == '4':
        # Gerar relatório
        total_eventos = len(eventos)
        eventos_apos_data = 0
        relatorio_participantes = {}

        for evento in eventos.values():
            # strptime transforma string em um objeto datetime
            data_evento = datetime.strptime(evento['data'], "%d/%m/%Y")
            if data_evento > datetime(2025, 1, 1):
                eventos_apos_data += 1

            relatorio_participantes[evento['nome']] = len(evento['participantes'])

        print("\nRelatório:")
        print(f"Total de eventos cadastrados: {total_eventos}")
        print(f"Eventos após 01/01/2025: {eventos_apos_data}")
        for nome_evento, qtd_participantes in relatorio_participantes.items():
            print(f"  Evento '{nome_evento}' tem {qtd_participantes} participantes.")

        input('\nPressione qualquer tecla para continuar...')
    else:
        print('Escreveu erradão')