import os


os.system('cls')

numero = str(input('Diga um número inteiro com 4 casas: '))

if int(numero) > (9999) or int(numero) < (0000):
    print('O número não possui 4 casas')
else:
    separar = " ".join(numero)
    print(separar)
    print(' ')
    print(f'o número {numero} tem {separar[6]} unidades')
    print(f'o número {numero} tem {separar[4]} dezenas')
    print(f'o número {numero} tem {separar[2]} centenas')
    print(f'o número {numero} tem {separar[0]} milhares')