
import os

os.system('cls')

# Entrada
numero = float(input('Digite um número: '))
resposta = '' 

# Condicional
if numero % 2 == 0:
        resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

# Saída
print(resposta)
print('Fim do Programa!\n') # \n salta uma linha
print('-'*70)