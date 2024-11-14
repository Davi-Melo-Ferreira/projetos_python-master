# Faça um programa que calcule os números primos em um fim pré-determinado pelo usuário.
import os


os.system('cls')

inc = int(input('Diga um número para o início: '))
fim = int(input('Diga um número para o fim: '))

for primos in range(inc, fim):
    divisores = 0
    for var_a in range(inc, fim + 1):
        if primos % var_a == 0:
            divisores += 1
    if divisores == 2:
        print(primos, end='|')
print('FIM')