import os
import random
import math

os.system('cls')

num = random.randint(0, 100)
num2 = random.randint(0, 100)

print(f'O número aleatório escolhido foi: {num}')

#calculos matematicos
raiz = math.sqrt(num)
print('-'*70)
print('Raiz')
print(f'Raiz de {num} = {raiz}')
print('.'*70)

# Potencia
potencia = math.pow(num, 2)
print('-'*70)
print('Potência(elevado a 2)')
print(f'Potência: {potencia}')
print('.'*70)

# seno, cosseno e tangente
print('-'*70)
print('SENO, COSSENO E TANGENTE ')
radiano = math.radians(num)
print(f'Radiano: {radiano}')
seno = math.sin(radiano)
print(f'Seno: {seno}')
cosseno = math.cos(radiano)
print(f'Cosseno: {cosseno}')
tangente = math.cos(radiano)
print(f'Tangente: {tangente}')
print('.'*70)

print('-'*70)
print('HIPOTENUSA')
hipotenusa = math.hypot(num, num2)
print(f'Hipotenusa: {hipotenusa}')
print('.'*70)
