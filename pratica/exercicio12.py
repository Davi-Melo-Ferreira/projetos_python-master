# dAB² = (xB – xA)² + (yB – yA)²
import os
import math

os.system('cls')

x1 = int(input('Digite um valor: '))
x2 = int(input('Digite um valor: '))
y1 = int(input('Digite um valor: '))
y2 = int(input('Digite um valor: '))

# processamento

dab = ((x2 - x1) ** 2) + ((y1 - y2) ** 2)
raiz = math.sqrt(dab)
print(raiz)