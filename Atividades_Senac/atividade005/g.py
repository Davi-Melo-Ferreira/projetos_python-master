# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.
import os


os.system('cls')

intervalo = int(input('Diga um número para o intervalo: '))

for c in range(1, intervalo + 1):
    if c == 4:
        continue
    if c <= 5:
        print(c)
    elif c % 2 != 0 and c % 3 != 0 and c % 5 != 0:
        print(c)
print('FIM')