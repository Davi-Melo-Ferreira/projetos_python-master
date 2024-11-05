import os


os.system('cls')

nome = input('Diga seu Nome: ')

nome_menor = nome.lower()
if 'oliveira' in nome_menor:
    print('O sobrenome Oliveira está presente')
else:
    print('O sobrenome Oliveira NÃO está presente')