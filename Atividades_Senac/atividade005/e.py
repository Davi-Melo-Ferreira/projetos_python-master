# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os


os.system('cls')

cont_par = 0
soma_par = 0

for c in range(0, 100, 2):
    cont_par += 1
    soma_par += c
print(f'Contador de par: {cont_par}')
print(f'Soma de par: {soma_par}')