import os
import math

os.system('cls')

valor = int(input('Diga um valor: '))

# Processamento pra fatorial x!
if valor <= 0:
    print('ERRO')
else:
    fatorial = math.factorial(valor)
    print(f'O fatorial de {valor}! é: {fatorial}')
