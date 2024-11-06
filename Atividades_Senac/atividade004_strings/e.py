#Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.
import os


os.system('cls')

frase = input('Diga uma frase: ')
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

soma = a + e + i + o + u

print(f'As vogais foram usadas {soma} vezes')