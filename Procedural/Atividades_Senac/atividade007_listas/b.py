# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os
import random

os.system('cls')

for j in range(6):
    lista = []
    for i in range(51):

        lista.append(random.randint(1, 100))
        qntd = len(lista)
        if qntd > 49:
            break
    print(lista)