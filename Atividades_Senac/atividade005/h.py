#Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela
import os


os.system('cls')

inc = int(input('Digite um valor para o início: '))
fim = int(input('Digite um valor para o fim: '))
intv = int(input('Digite um valor para o intervalo: '))

for c in range(inc, fim, intv):
    if c == 1:
        print('Não irei mostrar o 1,')
        continue
    if c == 2:
        print('Não irei mostrar o 2,')
        continue
    if c == 3:
        print('Não irei mostrar o 3,')
        continue
    print(c)