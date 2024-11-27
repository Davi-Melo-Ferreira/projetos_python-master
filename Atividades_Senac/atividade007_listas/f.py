# Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random

os.system('cls')

lista = []
lista_a = []
lista_d = []

for i in range(1, 11):
    lista.append(random.randint(1, 100))
print(lista)

lista_a = lista.copy()
lista_d = lista.copy()

lista_a.sort()
lista_d.sort(reverse=True)

print(f'Lista ascendente: {lista_a}')
print(f'Lista descendente: {lista_d}')