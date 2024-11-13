# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')

for c in range(1, 101):
    if c % 2 == 0:
        soma = c + c
        print(soma)
print('FIM')