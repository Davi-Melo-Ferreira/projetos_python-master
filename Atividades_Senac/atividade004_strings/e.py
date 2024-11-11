#Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.
import os


os.system('cls')

frase = input('Diga uma frase: ')
frasem = frase.lower()
a = frasem.count('a')
e = frasem.count('e')
i = frasem.count('i')
o = frasem.count('o')
u = frasem.count('u')

soma = a + e + i + o + u
print(f'A vogal A aparece: {a} vezes')
print(f'A vogal E aparece: {e} vezes')
print(f'A vogal I aparece: {i} vezes')
print(f'A vogal O aparece: {o} vezes')
print(f'A vogal U aparece: {u} vezes')
print('.'*70)
print(f'As vogais foram usadas {soma} vezes')