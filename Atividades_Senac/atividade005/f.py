# Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')

for loop in range(2, 101):
    divisores = 0
    for loop2 in range(1, loop + 1):
        if loop % loop2 == 0:
            divisores += 1
    if (divisores == 2):
        print(loop, end='|')