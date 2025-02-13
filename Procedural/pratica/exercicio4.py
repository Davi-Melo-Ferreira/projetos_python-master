#area = base x altura
#perimetro = 2 * (base + altura)
import os
import math

os.system('cls')

base = float(input('Diga o valor da Base: '))
altura = float(input('Diga o valor da Altura: '))

if base < 0 or altura < 0:
    print('Erro')
else:
    area = base * altura
    perimetro = 2 * (base + altura)

    print(f'A área é {area} e o perímetro é {perimetro}')