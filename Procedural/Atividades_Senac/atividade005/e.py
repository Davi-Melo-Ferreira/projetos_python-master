# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')

qntd_par = 0

for c in range(0, 100, 2):
    qntd_par += 1
print(f'Quantidade de pares encontrados: {qntd_par}')