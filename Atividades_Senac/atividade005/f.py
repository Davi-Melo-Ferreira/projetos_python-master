# Faça um programa que imprima os números primos entre 0 e 100.
# CÓDIGO PORCO
import os


os.system('cls')

for c in range(1, 101):
    if c == 4:
        continue
    if c <= 5:
        print(c)
    elif c % 2 != 0 and c % 3 != 0 and c % 5 != 0:
        print(c)
print('FIM')
