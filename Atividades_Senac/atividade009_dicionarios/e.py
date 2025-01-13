import os

lista = [
    {1:{'nome':'davi', 'nascimento':'24032006', 'matricula':'369'}},
    {2:{'nome':'thiago', 'nascimento':'30032005', 'matricula':'167'}},
    {3:{'nome':'joao', 'nascimento':'12092006', 'matricula':'282'}},
    {4:{'nome':'arthur', 'nascimento':'20051999', 'matricula':'937'}},
    {5:{'nome':'lucas', 'nascimento':'13102008', 'matricula':'191'}},
]

while True:
    os.system('cls')

    print('Menu de Opções:'
          '\n1. Modificar uma matrícula.'
          '\n2. Adicionar uma matrícula.'
          '\n3. Remover uma matrícula.'
          '\n4. Mostrar o dicionário.')
    opcao = input('\nDigite uma das opções(1, 2, 3, 4): ')
    if opcao == '1':
        escolha0 = int(input('De qual número você deseja modificar?: '))
        escolha1 = escolha0 - 1
        escolha2 = str(input('O que você deseja modificar?'
                            '(nome, nascimento, matricula): ')).lower()
        chave_principal = list(lista[escolha1].keys())[0]
        novo_valor = input(f"Digite o novo valor para '{escolha2}': ")
        lista[escolha1][chave_principal][escolha2] = novo_valor

        print("\nDicionário atualizado:")
        print('\nPressione qualquer tecla para continuar...')

    if opcao == '2':
        nome = input('Digite o nome do Aluno: ')
        nasc = int(input('Digite o ano de nascimento(ex:24032005): '))
        matricula = int(input('Digite o número de matrícula(ex:123): '))
        novo_id = len(lista) + 1 # se o último dic for 4 ent o próximo será 5
        lista.append({novo_id: {'nome': nome, 'nascimento': nasc, 'matrícula': matricula}})
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '3':
        escolha_3 = int(input('De qual número você deseja remover?: '))
        ind_escolha = escolha_3 - 1
        if 0 <= ind_escolha < len(lista):
            del lista[ind_escolha]
            
            for i, dicionario in enumerate(lista):
                chave_antiga = list(dicionario.keys())[0]
                dic_novo = {i + 1: dicionario[chave_antiga]}
                lista[i] = dic_novo
                
            print(f'Matrícula {escolha_3} removida com sucesso!')
        else:
            print('Número inválido! Nenhuma matrícula foi removida.')
        input('\nPressione qualquer tecla para continuar...')

    if opcao == '4':
        cont_nasc = 0
        cont_impar = 0
        for dicionario in lista:
            for id_lista, elementos in dicionario.items():
                print(id_lista)
                for key, value in elementos.items():
                    print(f'{key} : {value}')
                    if key == 'nascimento' and int(value) % 10000 > 2000:
                        cont_nasc += 1
                    if key == 'matricula' and int(value) % 2 != 0:
                        cont_impar += 1
        print(f'Ao todo, {cont_impar} números de matrícula são ímpar.')
        print(f'Ao todo, {cont_nasc} alunos nasceram depois de 2000.')
        input('\nPressione qualquer tecla para continuar...')