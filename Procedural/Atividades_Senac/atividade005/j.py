# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.
import os


os.system('cls')

qntd_impar = 0
soma_impar = 0

for c in range(1, 101, 2):
    qntd_impar += 1
    soma_impar += c
print(f'Quantidade de números ímpares = {qntd_impar}')
print(f'Soma de números ímpares = {soma_impar}')