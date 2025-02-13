import os
import random

os.system('cls')

for i in range(1,14):
    pegar = input('Pegar uma carta?: ').lower()
    if pegar == 'sim':
        carta = random.randint(1, i)
        if i == 1:
            