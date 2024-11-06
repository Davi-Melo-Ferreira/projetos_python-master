import os


os.system('cls')

nome = input('Diga um nome completo: ')

lista = nome.split()
lista_invert = lista[::-1]
print(f'{lista[0]} {lista_invert[0]}')