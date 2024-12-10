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
        '\n1. Alterar o valor de uma ferramente'
        '\n2. Mostrar o dicionário de ferramentas'
        )
    
    opcao = input('Qual você irá escolher?: ')

    if opcao == '1':
        chave = input('de qual chave você quer mudar o valor?: ')
        for elemento in ferramentas:
            if elemento == chave:
                valor_novo = input(f'{elemento}, insira o valor novo: ')
                valor_updatar = ferramentas.update([elemento, valor_novo])
    input('Conluído, pressione ENTER para continuar...')

    if opcao == '2':
        break
print(ferramentas)