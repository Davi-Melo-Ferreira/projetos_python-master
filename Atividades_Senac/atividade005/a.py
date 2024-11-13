# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal
import os


os.system('cls')

for c in range(1, 100 + 1):
    print(c, end=' | ')
    if c % 10 == 0:
        print('\n')
print('FIM')
