# Faça um programa que imprima os números pares entre 0 e 100.
import os


os.system('cls')

for c in range(0, 100, 2):
    if c % 10 == 0:
        print(c, '\n')
    print(c, end="|")