import os
import random
import string

os.system('cls')
alph = 'abcdefghijklmnopqrstuvwxyz'

letras = string.ascii_letters
numeros = string.digits
caracteres = ['@', '#', '!']
lista = [letras, caracteres, numeros]
senha = ''


while len(senha) < 12:
    senha += random.choice(random.choice(lista))
print(senha)
