# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
import os


os.system('cls')

frase = input('Diga uma frase: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u']
lista = []
for letra in frase:
    if letra in vogais:
        lista.append(letra)
print(lista[::-1])