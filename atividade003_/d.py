import os
import math

os.system('cls')

angulo = int(input('Diga o valor do angulo: '))

sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'Seno: {sin:.2f}, Cosseno: {cos:.2f}, Tangente: {tan:.2f}.')
