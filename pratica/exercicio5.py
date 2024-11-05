import os
import math

os.system('cls')

valor = int(input('Diga um valor: '))
if valor <= 0:
    print('ERRO')
else:
    fatorial = math.factorial(valor)
    print(fatorial)
