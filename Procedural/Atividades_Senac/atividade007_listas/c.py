# Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
import os
import random

os.system('cls')

for i in range(1, 6):
    lista = []
    for j in range(1, 51):
        lista.append(random.randint(1, 100))
        lista.sort()
        if len(lista) > 49:
            break          
    print(f'{i}ª Lista: {lista}\n')
    