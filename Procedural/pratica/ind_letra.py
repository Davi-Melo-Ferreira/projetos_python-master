import os
import random

os.system('cls')

# imprimir uma palavra em seus respectivos números no alfabeto
alph = ' abcdefghijklmnopqrstuvwxyz'

entrada = input('Digite uma palavra: ').lower().replace(' ','')
    
for char in entrada:
    verificar = alph.index(char)
    print(verificar, end=' ')