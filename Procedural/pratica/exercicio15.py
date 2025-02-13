# faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
import os


os.system('cls')

for c in range(1, 50):
    if c % 2 == 0:
        soma = c + c
        print(soma)
print('FIM')