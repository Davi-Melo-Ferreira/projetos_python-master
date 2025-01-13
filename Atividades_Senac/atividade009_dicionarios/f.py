# f
import os

# Lista de pessoas
lista = [
    {1: {'nome': 'João', 'idade': 25, 'peso': 70.5, 'altura': 1.75}},
    {2: {'nome': 'Maria', 'idade': 30, 'peso': 60.2, 'altura': 1.68}},
    {3: {'nome': 'Carlos', 'idade': 28, 'peso': 80.3, 'altura': 1.80}},
    {4: {'nome': 'Ana', 'idade': 22, 'peso': 55.0, 'altura': 1.65}},
    {5: {'nome': 'Pedro', 'idade': 35, 'peso': 90.7, 'altura': 1.85}}
]

while True:
    os.system('cls')
    # Exibindo dicionário antes da remoção
    print("\nDicionário(antes da exclusão):")
    for dicionario in lista:
        for id_lista, elementos in dicionario.items():
            print(f'\nPessoa: {id_lista}')
            for key, value in elementos.items():
                print(f'{key}: {value}')
    input('\nPressione qualquer tecla para continuar...')


    # Removendo a chave "peso" de cada dicionário
    for dicionario in lista:
        for elementos in dicionario.values():
            if 'peso' in elementos:
                del elementos['peso']

    # Exibindo dicionário após a remoção
    print("\nDicionário(após a exclusão do 'peso'):")
    for dicionario in lista:
        for id_lista, elementos in dicionario.items():
            print(f'\nPessoa: {id_lista}')
            for key, value in elementos.items():
                    print(f'{key}: {value}')
    input('\nPressione qualquer tecla para continuar...')

    # Sair do programa
    print("\nSaindo do programa...")
    break
