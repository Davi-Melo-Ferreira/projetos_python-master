# Simulação de Lançamento de Dados
import os
import math
import random

os.system('cls')

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print(dado1, dado2)
soma = dado1 + dado2
raiz = math.sqrt(soma)
print(soma)
print(raiz)
