import os
import random

os.system('cls')

num = random.randint(1, 2)

pergunta = int(input('Qual número estou pensando?: '))

if pergunta == num:
    print('acertou')
else:
    print('errou')