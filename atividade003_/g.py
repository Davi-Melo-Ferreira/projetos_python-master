import os
import math

os.system('cls')

a = int(input('Diga o valor de a: '))
b = int(input('Diga o valor de b: '))
c = int(input('Diga o valor de c: '))

delta = (b ** 2) - (4 * a * c)
print(f'Valor de Delta: {delta}')

if delta <= 0:
    print('Valor inválido')
else:
    raiz_delta = math.sqrt(delta)
    baskara1 = (-b + raiz_delta) / (2 * a)
    baskara2 = (-b - raiz_delta) / (2 * a)

print(f'O valor de báskara é {baskara1} ou {baskara2}')