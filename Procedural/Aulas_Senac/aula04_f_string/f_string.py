# Importar Biblioteca
import os

# Importa data, hora e ano
import datetime

# limpar terminal
os.system('cls')


print('»' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('»' * 70)

# Entrada
nome = input('Entre com um Nome: ')
peso = input('Entre com um Peso: ')
altura = input('Entre com uma Altura: ')

# Entrada com Casting
nascimento = int(input('Ano de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Nome do Bairro: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o número: '))

#Processando: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saída
print('-'*70)
print('SAÍDA DE DADOS')
print('='*70)
print('Nome..............:', nome)
print('Data de Nascimento:', nascimento)
print('Peso..............:', peso)
print('Altura............:', altura)

# Saída Interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP..............:{cep}')
print(f'Bairro...........:{bairro}')
print(f'rua..............:{rua}')
print(f'numero...........:{numero}')
print('-'*70)
print('')