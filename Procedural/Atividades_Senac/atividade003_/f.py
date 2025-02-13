import os
import random

os.system('cls')

aleatorio = random.randint(1, 10)
duvida = int(input('Que número estou pensando DE 1 A 10?: '))

if duvida == aleatorio:
    print('Parabéns!!')
else: 
    print('Você errou!!')