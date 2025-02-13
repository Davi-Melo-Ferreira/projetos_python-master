# Importar Biblioteca
import os


# Limpar Terminal
os.system('cls')

# Entrada
numero = int(input('Digite um Número Inteiro: '))
resposta = ''

# Processamento
if numero % 2 == 0:
    resposta = (f'O número {numero} é ímpar')
else:
    resposta = (f'O número {numero} não é ímpar')

# Saída
print (resposta)