# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.
import os


os.system('cls')

lista = []
listap = []
listai = []

for i in range(1, 8):
    nums = int(input(f'Digite o {i}º número: '))
    lista.append(nums)
    
for i in lista:
    if i % 2 == 0:
        listap.append(i)
    else:
        listai.append(i)
print(f'Lista de números pares: {listap}')
print(f'Lista de números ímpares: {listai}')