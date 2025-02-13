import os


os.system('cls')

ferramentas = {
    "Chave de Fenda": "aperta ou afrouxa parafuso.",
    "Alicate": "Segura, torce ou corta fios e materiais.",
    "Martelo": "Bate em objetos, como pregos ou peças.",
    "Serrote": "Corta madeira, plásticos e outros materiais sólidos.",
    "Chave Inglesa": "Aperta ou afrouxa porcas e parafusos de diferentes tamanhos."
}

while True:
    print('Menu de Opções'
        '\n1. Alterar o valor de uma ferramenta'
        '\n2. Mostrar o dicionário de ferramentas'
        )
    
    opcao = input('\nQual você irá escolher?: ')

    if opcao == '1':
        chave = input('de qual chave você quer mudar o valor?: ')
        for elemento in ferramentas.keys():
            if elemento.lower() == chave.lower():
                valor_novo = input(f'{elemento}, insira o valor novo: ')
                ferramentas[valor_novo] = ferramentas.pop(elemento)
        input('Conluído, pressione ENTER para continuar...')

    if opcao == '2':
        print()
        print(ferramentas)
        print('Total de elementos:', len(ferramentas) * 2)
        print()

        # Imprimir em ordem alfabética o dicionário
        ferramentas_asc = dict(sorted(ferramentas.items()))
        print(ferramentas_asc)
        print()

        # Ver quantas ferramentas tem mais de uma palavra
        space = 0
        for elemento in ferramentas:
            if ' ' in elemento:
                space += 1
        print(f'Existem {space} ferramentas com mais de uma palavra no nome')
        print()