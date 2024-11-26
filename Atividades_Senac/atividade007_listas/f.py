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

lista.sort()
lista_a.append(lista)

lista.sort(reverse=True)
lista_d.append(lista)

print(f'Lista ascendente: {lista}')
print(f'Lista descendente: {lista}')