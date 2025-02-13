import os


os.system('cls')

nome = input('Diga um nome completo: ')

lista = nome.split()
print(f'{lista[0]} {lista[-1]}')