import os


os.system('cls')

numero = str(input('Diga um número inteiro com 4 casas: '))

separar = " ".join(numero)
print(f'o número {numero} tem {separar[6]} unidades')
print(f'o número {numero} tem {separar[4]} dezenas')
print(f'o número {numero} tem {separar[2]} centenas')
print(f'o número {numero} tem {separar[0]} milhares')