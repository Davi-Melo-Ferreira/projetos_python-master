# Faça um programa que imprima os números pares entre 0 e 100.
import os


os.system('cls')

for c in range(1, 100 + 1):
    if c % 2 == 0:
        print(c)
print('FIM')
