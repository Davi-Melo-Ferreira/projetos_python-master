# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.
import os


os.system('cls')

lista = []
lista_pares = []
lista_impares = []

for i in range(1, 8):
    nums = int(input(f'Digite o {i}º número: '))
    lista.append(nums)
    
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f'Lista de números pares: {lista_pares}')
print(f'Lista de números ímpares: {lista_impares}')