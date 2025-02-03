# Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random

os.system('cls')

lista = []
lista_ascendente = []
lista_descendente = []

for i in range(1, 11):
    lista.append(random.randint(1, 100))
print(lista)

lista_ascendente = lista.copy()
lista_descendente = lista.copy()

lista_ascendente.sort()
lista_descendente.sort(reverse=True)

print(f'Lista ascendente: {lista_ascendente}')
print(f'Lista descendente: {lista_descendente}')