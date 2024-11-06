#Faça um programa que leia uma frase e depois exiba na tela:
#A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.


import os


os.system('cls')

frase = input('Diga uma frase: ')
frasem = frase.lower()
fraseM = frase.upper()
quantidade = len(frase)
lista = frase.split()
quantidade2 = len(lista[1])

print(f'{frasem}')
print(f'{fraseM}')
print(f'{quantidade}')
print(f'{quantidade2}')